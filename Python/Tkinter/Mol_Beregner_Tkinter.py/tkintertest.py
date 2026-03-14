import tkinter as tk
import ttkbootstrap as ttk

window = ttk.Window(themename="minty")
#Endrer fargen på selve window
window.config(bg = "lightblue")

#Gjør at frame strekker seg helt ut til enden av window
#columnconfigure(kolonne, hvor mye)
#rowconfigure(rekke, hvor mye)
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight = 10)
window.rowconfigure(1, weight=1)


tittel_frame = tk.Frame(
    window, 
    bg = "lightgreen", 
    padx = 10, 
    pady = 10,
    #Hvor tjukk kanten er
    bd = 1, 
    #Hvilken stil
    relief = "solid"
)
tittel_frame.grid(
    column = 0, 
    row = 0, 
    sticky= "nsew", 
    columnspan= 2, 
    ipadx = 50
)
tittel_label = tk.Label(
    tittel_frame, 
    text = "HEIEHEI",
    bg = "lightblue", 
    font = ("Arial", 30)
)
tittel_label.pack(anchor="w")

a_frame = tk.Frame(
    window, 
    bg = "mistyrose", 
    padx = 10, 
    pady = 10, 
    bd = 1, 
    relief = "raised"
)
a_frame.grid(
    column = 0, 
    row = 1, 
    sticky = "nsew", 
    columnspan= 1, 
)
a_label = tk.Label(
    a_frame, 
    bg = "lightblue", 
    text = "WAT DA SIGMA"
)
a_label.pack(anchor= "w")

window.mainloop()