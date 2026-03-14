import tkinter as tk
import math
import random

window = tk.Tk()
window.title("TV_Skjerm")
window.geometry("700x500")

frame = tk.Frame(
    window, 
    padx = 10, 
    pady= 10, 
    bd  =0, 
    relief = "solid"
)
frame.grid(
    column = 0, 
    row = 1, 
    sticky= "nsew", 
    ipadx  = 50
)
canvas = tk.Canvas(
    frame, 
    width= 680, 
    height= 480, 
    bg = "black"
)
canvas.grid(
    column = 0, 
    row = 0
)

#tv objekt --------------------------
x1, y1 = 100, 100
x2, y2 = 180, 150
dx1, dy1 = 2.5, 2.5
tv = canvas.create_rectangle(
    x1, 
    y1, 
    x2, 
    y2, 
    fill = "lightgreen", 
    outline= "black"
)

tv_tekst = canvas.create_text(
    #Posisjoner, men sentrum for objekt tv
    (x1 + x2) / 2, 
    (y1 + y2) / 2, 
    text = "TV", 
    fill = "black", 
    font = ("Arial", 14, "bold")
)

def flytt_tv():
    global dx1, dy1

    canvas.move(tv, dx1, dy1)
    canvas.move(tv_tekst, dx1, dy1)

    pos1 = canvas.coords(tv)
    
    farger = ["red", "green", "blue", "yellow", "magenta", "cyan", "orange"]

    if pos1[0] <= 0 or pos1[2] >= 680:
        dx1 *= -1
        canvas.itemconfig(tv, fill = random.choice(farger))

    if pos1[1] <= 0 or pos1[3] >= 480:
        dy1 *= -1
        canvas.itemconfig(tv, fill = random.choice(farger))

    window.after(10, flytt_tv)

flytt_tv()

window.mainloop()