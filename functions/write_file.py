import os

from google.genai import types

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description=f"Write content to the specified file, constrained to the working directory. Will overwrite any existing file with the same name, will create new file if not.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path for the file to write the contents, relative to the working directory. Must be provided",

            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content of the file to write. Must be provided",
            )
        },
    ),
)

def write_file(working_directory, file_path, content):
    try:
        working_directory = os.path.join(os.getcwd(), working_directory)
        abs_path = os.path.realpath(os.path.join(working_directory, file_path))

        if not os.path.commonpath([abs_path, working_directory]) == working_directory:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        with open(abs_path, 'w') as f:
            f.write(content)

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f'Error: {e}'