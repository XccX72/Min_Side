import tkinter as tk
import tkinter.font as tkf
from Calculator import meny


window = tk.Tk()              
window.title("Kalkulator")    
label = tk.Label(window, text="Kalkulator 1.0", font=("Helvetica", 80))
label.grid(column= 0, row = 0, padx=75, pady=10)

pluss_font = tkf.Font(family = "Helvetica", size = 30, weight = "bold")
pluss = tk.Button(
    window, 
    text = "Pluss",
    font = pluss_font, 
    bg = "lightblue"
)

minus_font = tkf.Font(family = "Helvetica", size = 30, weight = "bold")
minus = tk.Button(
    window, 
    text = "Minus", 
    font = minus_font, 
    bg = "lightblue"
)

ganging_font = tkf.Font(family = "Helvetica", size = 30, weight = "bold")
ganging = tk.Button(
    window, 
    text = "Ganging", 
    font = ganging_font, 
    bg = "lightblue"
)

deling_font = tkf.Font(family = "Helvetica", size = 30, weight = "bold")
deling = tk.Button(
    window, 
    text = "Brøk",
    font = deling_font,
    bg = "lightblue"
)


pluss.grid(row=2, column=1, padx = 10, pady = 10, ipadx = 20, ipady = 30)
minus.grid(row=1, column=1, padx = 10, pady = 10, ipadx = 20, ipady = 30)
ganging.grid(row=4,column=1, padx= 10, pady = 10, ipadx = 20, ipady = 30)
deling.grid(row=3,column=1, padx = 10, pady = 10, ipadx = 20, ipady = 30)


window.mainloop()