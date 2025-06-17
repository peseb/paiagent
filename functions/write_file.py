import os
from functions.util import get_absolute_paths, validate_path


def write_file(working_directory: str, file_path: str, content: str):
    abs_path_workdir, abs_file_path = get_absolute_paths(working_directory, file_path)
    err = validate_path(abs_path_workdir, abs_file_path, file_path)
    if err != None:
        return err
    
    try:
        mode = "w" if os.path.exists(abs_file_path) else "x"
        f = open(abs_file_path, mode)
        f.write(content)
        f.close()

        return f"Successfully wrote to \"{file_path}\" ({len(content)} characters written)"
    except Exception as e:
        return f"Error: {e}"