import tkinter as tk

def skriv_ut():
    hilsen.configure(text=f"Hallo {navn.get()}!")

root = tk.Tk()

navn = tk.Entry(root)
navn.insert(0, "hva heter du?")
navn.pack()

tk.Button(root, text="Les navn", command=skriv_ut).pack()

hilsen = tk.Label(root)
hilsen.pack()

root.mainloop()

