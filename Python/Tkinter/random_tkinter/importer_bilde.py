import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk()
window.geometry("500x500")

bilde = Image.open("Tkinter/random_tkinter/vebjørn.png")
bilde_bla = ImageTk.PhotoImage(bilde)

a = tk.Label(
    window, image = bilde_bla
)
a.pack()
window.mainloop()