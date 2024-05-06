import ast
import os

def count_functions(file_path):
    total_functions = 0
    with open(file_path, "r") as f:
        try:
            tree = ast.parse(f.read(), filename=file_path)
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    total_functions += 1
        except Exception as e:
            print(f"Error parsing {file_path}: {e}")
    return total_functions

def count_functions_in_project(project_dir):
    total_project_functions = 0
    for root, dirs, files in os.walk(project_dir):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                total_project_functions += count_functions(file_path)
    return total_project_functions

     