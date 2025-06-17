# from subdirectory.filename import function_name
from functions.run_python import run_python_file

r = run_python_file("calculator", "main.py")
print(r)
r = run_python_file("calculator", "tests.py")
print(r)
r = run_python_file("calculator", "../main.py")
print(r)
r = run_python_file("calculator", "nonexistent.py")
print(r)