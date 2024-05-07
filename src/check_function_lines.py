import ast
import os

def check_long_functions(file_path, max_lines=15):
    with open(file_path, 'r') as file:
        code = file.read()
    
    tree = ast.parse(code)

    for node in ast.walk(tree):
        print(type(node).__name__)
        if isinstance(node, ast.FunctionDef):
            function_name = node.name
            function_lines = node.end_lineno - node.lineno + 1
            if function_lines > max_lines:
                return f"Warning: Function '{function_name}' in {os.path.basename(file_path)} exceeds {max_lines} lines (lines: {node.lineno}-{node.end_lineno})"
