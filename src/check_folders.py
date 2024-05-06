import os

def check_nested_folders(directory):
    for root, dirs, files in os.walk(directory):
        """line calculates the depth of nesting for the current directory by:
            Removing the initial part of the root path corresponding to the directory being checked.
            Counting the occurrences of the directory separator os.sep in the remaining path.
        """
        depth = root[len(directory) + 1:].count(os.sep) 
        if depth > 3:
            return f"Warning: '{root}' has more than 3 levels of nested folders!"