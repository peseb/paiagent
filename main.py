import os
import sys
from dotenv import load_dotenv
from google import genai


load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)
prompt = ""

arguments = sys.argv
if len(arguments) > 1:
    prompt = arguments[1]
else:
    print(("No prompt given. Exiting..."))
    exit(1)

model = "gemini-2.0-flash-001"
response = client.models.generate_content(model=model, contents=prompt)
print("response: ", response.text)
print("Prompt tokens:", response.usage_metadata.prompt_token_count)
print("Response tokens:", response.usage_metadata.candidates_token_count)