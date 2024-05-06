import os

def check_file_mix(directory):
    python_file_count = 0
    non_python_file_count = 0
    config_file_count = 0

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                python_file_count += 1
            elif file.endswith(('.conf', '.cfg', '.ini', '.yaml', '.yml')):
                config_file_count += 1    
            elif not file.endswith('.py'):
                non_python_file_count += 1

    if python_file_count > 0 or non_python_file_count > 0 or config_file_count > 0:
        return python_file_count,non_python_file_count,config_file_count