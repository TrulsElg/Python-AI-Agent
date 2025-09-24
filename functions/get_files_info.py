import os

from config import MAX_CHARACTERS_IN_FILE
from google.genai import types

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
    ]
)

def get_files_info(working_directory, directory="."):

    try:
        working_directory = os.path.join(os.getcwd(), working_directory)
        abs_path = os.path.realpath(os.path.join(working_directory, directory))

        if not os.path.commonpath([abs_path, working_directory]) == working_directory:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if not os.path.isdir(abs_path):
            return f'Error: "{directory}" is not a directory'

        directory_content_string = ""

        for entry in sorted(os.listdir(abs_path)):
            entry_path = os.path.join(abs_path, entry)
            size = os.path.getsize(entry_path)
            is_dir = os.path.isdir(entry_path)
            if directory_content_string:
                directory_content_string += f"\n - {entry}: file_size={size} bytes, is_dir={is_dir}"
            else:
                directory_content_string = f" - {entry}: file_size={size} bytes, is_dir={is_dir}"

        return directory_content_string
    except Exception as e:
        return f'Error: {e}'


def get_file_content(working_directory, file_path):
    try:
        working_directory = os.path.join(os.getcwd(), working_directory)
        abs_path = os.path.realpath(os.path.join(working_directory, file_path))

        if not os.path.commonpath([abs_path, working_directory]) == working_directory:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(abs_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        with open(abs_path, 'r') as f:
            file_contents = f.read()
            if len(file_contents) > MAX_CHARACTERS_IN_FILE:
                return file_contents[0:MAX_CHARACTERS_IN_FILE] + \
                    f'[...File "{file_path}" truncated at {MAX_CHARACTERS_IN_FILE} characters]'
            else:
                return file_contents

    except Exception as e:
        return f'Error: {e}'