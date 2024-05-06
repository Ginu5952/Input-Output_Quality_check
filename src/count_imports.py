import ast
import os



def count_imports(file_path):
    total_imports = 0
    with open(file_path, "r") as f:
        try:
            tree = ast.parse(f.read(), filename=file_path)
            for node in ast.walk(tree):
                if isinstance(node, ast.Import) or isinstance(node, ast.ImportFrom):
                    total_imports += 1
        except Exception as e:
            print(f"Error parsing {file_path}: {e}")
    return total_imports

def count_imports_in_project(project_dir):
    total_project_imports = 0
    for root, dirs, files in os.walk(project_dir):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                total_project_imports += count_imports(file_path)
    return total_project_imports
