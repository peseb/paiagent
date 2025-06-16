import os
from functions.get_files_info import get_files_info


def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        abs_path_workdir = os.path.abspath(working_directory)
        abs_filepath = os.path.abspath(os.path.join(abs_path_workdir, file_path))

        if not abs_filepath.startswith(abs_path_workdir):
            return f"Error: Cannot list \"{abs_filepath}\" as it is outside the permitted working directory"
        
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