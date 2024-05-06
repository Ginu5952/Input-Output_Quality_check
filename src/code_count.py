# read :- return string
#readlines :- return list of strings
# readline :- read first line
# seek :- set cursor position


import os 
# Create a function to count for a single file
from typing import TextIO 
import ast


 # Hide the main window

def count_code_line(o_file): 
    code_lines:int = 0 
    block_lines:int = 0 
    doc_strings:int = 0 
    doc_string_finished:bool = False 
    upper_hash = 0
 
    '''This is a 
    doc string
    '''

    """ thkljnm"""
    # what read method we can use
    while line := o_file.readline(): 
        line = line.strip()   # remove spaces at the left and right   
       
        if len(line) > 0: 
      
            if line.startswith("'''") or line.startswith('"""') and not doc_string_finished: 
                doc_strings += 1 
                doc_string_finished = True 
                continue 
            elif line.endswith("'''") or line.endswith('"""') and doc_string_finished: 
                doc_string_finished = False 
                continue 
        
            elif doc_string_finished:  
                continue 
            elif '#' in line:
                block_lines += 1
                
                if line.startswith('#'): 
                    upper_hash += 1
                
            code_lines += 1        
             
    return code_lines  - upper_hash, block_lines - 2, doc_strings 

        
def project_code_counter(path:str,code_line_counter) -> int: 
    # determine if 'path' is a file or a directory

    if os.path.isfile(path):
        file_basename = os.path.basename(path) # get base name name of text 
        if file_basename.startswith('.') or not file_basename.endswith('.py'): 
            
            return 0 
        with open(path) as o_file: 
            return code_line_counter(o_file) 
    
    return sum( 
        project_code_counter(os.path.join(dir_path,file),code_line_counter) 
        for dir_path,_,files in os.walk(path)  # _ is ignore second 
        for file in files 
    ) 

class example:
    pass

"""
ast stands for Abstract Syntax Trees.
 ast module provides functions to parse Python source code into
 an abstract syntax tree (AST) and to work with the resulting tree structure.
"""







     