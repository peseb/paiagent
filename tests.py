# from subdirectory.filename import function_name
from functions.get_file_content import get_file_content
from functions.get_files_info import get_files_info

res1 = get_file_content("calculator", "main.py")
print(res1)

res2 = get_file_content("calculator", "pkg/calculator.py")
print(res2)

res3 = get_file_content("calculator", "/bin/cat")
print(res3)