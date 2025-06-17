import os


def get_absolute_paths(working_directory: str, file_path: str | None):
    abs_path_workdir = os.path.abspath(working_directory)
    abs_filepath = os.path.abspath(os.path.join(abs_path_workdir, file_path)) if file_path != None else ""
    return abs_path_workdir, abs_filepath

def validate_path(working_dir: str, abs_file_path: str, file_path: str) -> str | None:
    if abs_file_path.startswith(working_dir):
        return None
    
    return f"Error: Cannot list \"{file_path}\" as it is outside the permitted working directory"