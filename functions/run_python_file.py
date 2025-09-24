import os
import subprocess


def run_python_file(working_directory, file_path, args=[]):
    try:
        working_directory = os.path.join(os.getcwd(), working_directory)
        abs_path = os.path.realpath(os.path.join(working_directory, file_path))

        if not os.path.commonpath([abs_path, working_directory]) == working_directory:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(abs_path):
            return f'Error: File "{file_path}" not found.'

        if not str(abs_path).endswith('.py'):
            return f'Error: "{file_path}" is not a Python file.'

        completed_process = subprocess.run((f"uv", "run", file_path, *args),
                                           cwd=working_directory,
                                           capture_output=True,
                                           text=True,
                                           timeout=30)

        if completed_process.stdout or completed_process.stderr:
            result = ""
            result += f"STDOUT: {completed_process.stdout}\n"
            result += f"STDERR: {completed_process.stderr}"
            if completed_process.returncode != 0:
                result += f"\nProcess exited with code: {completed_process.returncode}"
        else:
            result = "No output produced."

        return result

    except Exception as e:
        return f"Error: executing Python file: {e}"