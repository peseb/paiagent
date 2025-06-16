import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types



load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)
user_prompt = ""

arguments = sys.argv
if len(arguments) > 1:
    prouser_promptmpt = arguments[1]
else:
    print(("No prompt given. Exiting..."))
    exit(1)

verbose = False
if len(arguments) > 2 and arguments[2] == "--verbose":
    verbose = True

messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
]

model = "gemini-2.0-flash-001"
response = client.models.generate_content(model=model, contents=messages)
print("response: ", response.text)
if verbose:
    print("User prompt: {user_prompt}")
    print("Prompt tokens:", response.usage_metadata.prompt_token_count)
    print("Response tokens:", response.usage_metadata.candidates_token_count)