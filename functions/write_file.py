import os

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