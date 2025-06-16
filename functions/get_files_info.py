import os


def get_files_info(working_directory, directory=None):
    abs_path_workdir = os.path.abspath(working_directory)
    dir_path = os.path.abspath(os.path.join(abs_path_workdir, directory))
    if not os.path.isdir(dir_path):
        return f'Error: "{directory}" is not a directory'

    # directory_path = os.path.join(abs_path_directory, abs_path_directory)
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