import tkinter as tk
import os
from src.code_count import *
from src.check_folders import *
from src.check_function_lines import *
from src.check_python_files import *
from src.count_functions import *
from src.count_imports import *
from src.count_class import *
from src.bubble_animation import start_animation



file_path = os.path.join(os.getcwd(), 'src','code_count.py')
folder_path = os.path.join(os.getcwd(),'src')

class CustomAlert:
   
    def __init__(self, master,image_path):
        
        self.master = master
        self.master.title("Quality Check Report")
        self.image_path = image_path
        self.canvas = tk.Canvas(master, width=800, height=600)  # Adjusted canvas size
        self.canvas.pack()
        self.background_image = tk.PhotoImage(file=self.image_path)  # Load background image
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.background_image)  # Display background image
        
        count,block,doc = project_code_counter(file_path,count_code_line)
        nested_folders = check_nested_folders('src')
        check_function_lines = check_long_functions(file_path)
        python,nonpython,config = check_file_mix(folder_path)
        total_imports = count_imports_in_project(folder_path)
        total_functions = count_functions_in_project(folder_path)
        total_class = count_classes_in_project(folder_path)

      
        count_text = f"Total Number of lines in code_count.py:          {count}"
        block_text = f"Total Number of lines with # in code_count.py:   {block}"
        doc_text = f"Total Number of Doc Strings in code_count.py:     {doc}"
        nested_folder = f"{nested_folders}"
        python_files = f"Total Number of Python files inside src folder:            {python}"
        non_python_files = f"Total Number of Non Python files inside src folder:    {nonpython}"
        config_files = f"Total Number of Config files inside src folder:             {config}"
        imports = f"Total Number of import in the entire project:               {total_imports}"
        functions = f"Total Number of functions in the entire project:           {total_functions}"
        classes = f"Total Number of class in the entire project:                 {total_class}"
        
        self.canvas.create_text(10, 10, anchor=tk.NW, text=count_text, fill="white",font = ("Arial", 14))
        self.canvas.create_text(10, 30, anchor=tk.NW, text=block_text, fill="white",font = ("Arial", 14))
        self.canvas.create_text(10, 50, anchor=tk.NW, text=doc_text, fill="white",font = ("Arial", 14))
        self.canvas.create_text(10, 100, anchor=tk.NW, text=nested_folder, fill="white",font = ("Arial", 14))
        self.canvas.create_text(10, 120, anchor=tk.NW, text=check_function_lines, fill="white",font = ("Arial", 14))
        self.canvas.create_text(10, 160, anchor=tk.NW, text=python_files, fill="white",font = ("Arial", 14))
        self.canvas.create_text(10, 180, anchor=tk.NW, text=non_python_files, fill="white",font = ("Arial", 14))
        self.canvas.create_text(10, 220, anchor=tk.NW, text=config_files, fill="white",font = ("Arial", 14))
        self.canvas.create_text(10, 240, anchor=tk.NW, text=imports, fill="white",font = ("Arial", 14))
        self.canvas.create_text(10, 260, anchor=tk.NW, text=functions, fill="white",font = ("Arial", 14))
        self.canvas.create_text(10, 280, anchor=tk.NW, text=classes, fill="white",font = ("Arial", 14))

        start_animation(self.canvas)
