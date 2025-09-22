import os

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