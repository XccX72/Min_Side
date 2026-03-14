import tkinter as tk           # font er en submodul,
from tkinter import font      # som ikke kan kalles direkte med tk.
from PIL import Image, ImageTk # husk pip install Pillow

# Funksjon for å vise hilsen basert på inndata
def skriv_ut():
    hilsen.configure(text=f"Hallo {navn.get()}!")

root = tk.Tk()

# Endre standard skrift, gjelder ikke Entry-widget
default_font = tk.font.nametofont("TkDefaultFont")
default_font.configure(family="Arial", size=20)

# Endre tekst på tittellinjen
root.title("Inndata/Utdata")

# Legg til et bilde, krever from PIL import Image, ImageTk
bilde = Image.open("Tkinter/vebjørn.png")
bilde = bilde.resize((150, 150), Image.Resampling.LANCZOS)
bilde = ImageTk.PhotoImage(bilde)
tk.Label(root, image=bilde).grid(row=0, column=0, padx=5, pady=5)

# Lag en ramme for høyre del
frame = tk.Frame(root, padx=100, pady=100)
frame.grid(row=0, column=1, padx=5, pady=15)

navn = tk.Entry(frame, width=15, font=("Arial 20"))
navn.insert(0, "Hva heter du? ")
navn.grid(row=0, column=0, padx=5, pady=13)

tk.Button(frame, text="Les navn", command=skriv_ut, width=10) \
    .grid(row=0, column=1, padx=5)

hilsen = tk.Label(frame, width=50, bg="#008cff", fg="red", pady=100)
hilsen.grid(row=1, column=0, columnspan=2, pady=13)

root.mainloop()