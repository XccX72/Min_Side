import tkinter as tk
from tkinter import font
import PIL

def skriv_ut():
    hilsen.configure(text=f"Hallo {navn.get()}!")

root = tk.Tk()

default = tk.font.nametofont("TKdghfdfg")
default.configure(family="Arial", size = 20)


root.mainloop()