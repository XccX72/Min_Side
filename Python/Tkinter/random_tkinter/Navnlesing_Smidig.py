import tkinter as tk

def skriv_ut():
    hilsen.configure(text = f"Hallo {navn.get()}")

window = tk.Tk()

navn = tk.Entry(window)
navn.insert(0, "Hva heter du")
navn.pack()

tk.Button(
    window, text = "Les navn",
    command = skriv_ut
).pack()

label = tk.Label(text = " ").pack()

hilsen = tk.Label(window)
hilsen.pack()

window.mainloop()