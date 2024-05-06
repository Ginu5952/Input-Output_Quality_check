import tkinter as tk
from src.custom_alert import CustomAlert
import os


image_path = os.path.join(os.getcwd(),"images","image.png")


root = tk.Tk()


app = CustomAlert(root,image_path)
root.mainloop()

