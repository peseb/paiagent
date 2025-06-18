import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

from functions.call_function import call_function
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


loop_number = 0
while loop_number < 20:
    loop_number+=1
    response = client.models.generate_content(model=model, contents=messages, config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt))
    
    if response.candidates:
        for candidate in response.candidates:
            if candidate.content:
                messages.append(candidate.content)

    if response.function_calls:
        for function_call_part in response.function_calls:
            print(f"Calling function: {function_call_part.name}({function_call_part.args})")
            result = call_function(function_call_part, verbose)
            messages.append(result)
            function_response = result.parts[0].function_response.response # type: ignore
            if not function_response:
                raise Exception("No function response.")
            if verbose:
                print(f"-> {function_response}")
    else:
        print("response: ", response.text)
        break

    if verbose:
        print("User prompt: {user_prompt}")
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)
    if response.candidates:
        for candidate in response.candidates:
            if candidate.content:
                messages.append(candidate.content)