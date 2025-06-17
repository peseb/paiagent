import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

from helper import get_function_definitions



load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)
user_prompt = ""

arguments = sys.argv
if len(arguments) > 1:
    user_prompt = arguments[1]
else:
    print(("No prompt given. Exiting..."))
    exit(1)

verbose = False
if len(arguments) > 2 and arguments[2] == "--verbose":
    verbose = True

available_functions = get_function_definitions()

system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""

messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
]

model = "gemini-2.0-flash-001"
response = client.models.generate_content(model=model, contents=messages, config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt))
if response.function_calls:
    for function_call_part in response.function_calls:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
else:
    print("response: ", response.text)

if verbose:
    print("User prompt: {user_prompt}")
    print("Prompt tokens:", response.usage_metadata.prompt_token_count)
    print("Response tokens:", response.usage_metadata.candidates_token_count)