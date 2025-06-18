
from google.genai import types

from functions.get_file_content import get_file_content
from functions.get_files_info import get_files_info
from functions.run_python import run_python_file
from functions.write_file import write_file

def call_function(function_call_part: types.FunctionCall, verbose: bool=False):
    if verbose:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_call_part.name}")
    
    function_name = function_call_part.name if function_call_part.name else ""
    valid_functions = ["get_file_content", "get_files_info", "run_python_file", "write_file"]
    if function_name not in valid_functions:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"error": f"Unknown function: {function_name}"},
                )
            ],
        )
    
    res = None
    match function_name:
        case "get_file_content":
            res = get_file_content("./calculator", **function_call_part.args) # type: ignore
        case "get_files_info":
            res = get_files_info("./calculator", **function_call_part.args) # type: ignore
        case "run_python_file":
            res = run_python_file("./calculator", **function_call_part.args) # type: ignore
        case "write_file":
            res = write_file("./calculator", function_call_part.args["file_path"], function_call_part.args["content"]) # type: ignore
        case _:
            return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"error": f"Unknown function: {function_name}"},
                )
            ],
        )
    
    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_name,
                response={"result": res},
            )
        ],
    )

