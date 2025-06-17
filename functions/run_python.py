import os
import subprocess
from functions.util import get_absolute_paths, validate_path


def run_python_file(working_directory: str, file_path: str):
    abs_path_workdir, abs_file_path = get_absolute_paths(working_directory, file_path)
    err = validate_path(abs_path_workdir, abs_file_path, file_path)
    if err != None:
        return err.replace("list", "execute")
    
    if not os.path.exists(abs_file_path):
        return f"Error: File \"{file_path}\" not found."

    if not abs_file_path.endswith(".py"):
        return f"Error: \"{file_path}\" is not a Python file."
    
    try:
        result = subprocess.run(["python", abs_file_path], timeout=30, capture_output=True, text=True, cwd=abs_path_workdir)
        print("STDOUT:",result.stdout)
        print("STDERR:",result.stderr)
        if result.returncode != 0:
            print(f"Process exited with code {result.returncode}")
        if len(result.stdout) + len(result.stderr) == 0:
            print("No output produced")
    except Exception as e:
        print(f"Error: executing Pything file: {e}")