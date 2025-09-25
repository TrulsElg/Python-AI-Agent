import os
import sys

from dotenv import load_dotenv
from google import genai
from google.genai import types
from config import system_prompt, model_name
from functions.get_files_info import schema_get_files_info, schema_get_file_content
from functions.write_file import schema_write_file
from functions.run_python_file import schema_run_file
from functions.call_function import call_function

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
                schema_get_file_content,
                schema_write_file,
                schema_run_file,
            ]
        )

        for i in range(20):
            try:
                response = client.models.generate_content(
                    model= model_name,
                    contents=messages,
                    config=types.GenerateContentConfig(tools=[available_functions],
                                                       system_instruction=system_prompt)
                )

                for candidate in response.candidates:
                    messages.append(candidate.content)

                if verbose_output:
                    print(f"User prompt: {user_prompt}")
                    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
                    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

                if response.function_calls:
                    for function_call_part in response.function_calls:
                        # print(f"Calling function: {function_call_part.name}({function_call_part.args})")
                        call_result = call_function(function_call_part=function_call_part, verbose=verbose_output)

                        part = call_result.parts[0] if call_result.parts else None
                        if part is None:
                            raise ValueError("Function call returned no parts")

                        if not hasattr(part, "function_response"):
                            raise ValueError("Function call part missing function_response")

                        if not hasattr(part.function_response, "response") or not part.function_response.response:
                            raise ValueError("Function call did not return a response")

                        if verbose_output:
                            print(f"-> {call_result.parts[0].function_response.response}")

                        messages.append(types.Content(role="user", parts=call_result.parts))
                else:
                    if response.text:
                        print(response.text)
                        break
                    else:
                        if verbose_output:
                            print("Empty response with no tool calls; stopping.")
                        break
            except Exception as e:
                print(e)
                break

    else:
        print("No input provided")
        exit(1)

if __name__ == '__main__':
    main()