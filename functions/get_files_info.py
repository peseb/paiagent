import os

from functions.util import get_absolute_paths, validate_path


def get_files_info(working_directory: str, directory: str | None=None):
    abs_path_workdir, dir_path = get_absolute_paths(working_directory, directory)
    err = validate_path(abs_path_workdir, dir_path)
    if err != None:
        return err
    
    if not os.path.isdir(dir_path):
        return f'Error: "{directory}" is not a directory'

    if not dir_path.startswith(abs_path_workdir):
        return f'Error: Cannot list "{dir_path}" as it is outside the permitted working directory'

    result = ""
    dir_contents = os.listdir(dir_path)
    for entry in dir_contents:
        try:
            filepath = os.path.join(dir_path, entry)
            size = os.path.getsize(filepath)
            is_dir = os.path.isdir(filepath)
            result += f"{entry}: file_size={size} bytes, is_dir={is_dir}\n"
        except Exception as error:
            result += f"Error: {error}"
    
    return result