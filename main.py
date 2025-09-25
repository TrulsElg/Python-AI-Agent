import os
import sys

from dotenv import load_dotenv
from google import genai
from google.genai import types
from config import system_prompt, model_name
from functions.get_files_info import schema_get_files_info

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

def main():
    if len(sys.argv) > 1:
        verbose_output = False
        if len(sys.argv) > 2 and sys.argv[2] == "--verbose":
            verbose_output = True

        user_prompt = sys.argv[1]

        messages = [
            types.Content(role="user", parts=[types.Part(text=user_prompt)]),
        ]

        available_functions = types.Tool(
            function_declarations=[
                schema_get_files_info,
            ]
        )

        response = client.models.generate_content(
            model= model_name,
            contents=messages,
            config=types.GenerateContentConfig(tools=[available_functions],
                                               system_instruction=system_prompt)
        )

        if verbose_output:
            print(f"User prompt: {user_prompt}")
            print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
            print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

        if response.function_calls:
            for function_call_part in response.function_calls:
                print(f"Calling function: {function_call_part.name}({function_call_part.args})")
        else:
            print(response.text)

    else:
        print("No input provided")
        exit(1)

if __name__ == '__main__':
    main()