import os
from functions.util import get_absolute_paths, validate_path


def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        abs_path_workdir, abs_filepath = get_absolute_paths(working_directory, file_path)
        err = validate_path(abs_path_workdir, abs_filepath)
        if err != None:
            return err
        
        if not os.path.isfile(abs_filepath):
            return f"Error: File not found or is not a regular file: \"{abs_filepath}\""
        
        f = open(abs_filepath)
        file_contents = f.read()
        f.close()

        if len(file_contents) > 10000:
            file_contents = file_contents[:10000] + f"[...File \"{file_path}\" truncated at 10000 characters]"
        
        return file_contents
    except Exception as e:
        return f"Error: {e}"