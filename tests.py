# from subdirectory.filename import function_name
from functions.get_files_info import get_files_info

res1 = get_files_info("calculator", ".")
print(res1)

res2 = get_files_info("calculator", "pkg")
print(res2)

res3 = get_files_info("calculator", "/bin")
print(res3)

res4 = get_files_info("calculator", "../")
print(res4)