import tkinter as tk
import ttkbootstrap as ttk

window = ttk.Window(themename="minty")
window.geometry("300x200")
window.title("Alll")

# 1. Lag variabelen som skal holde på valget
valgt_alternativ = tk.StringVar(value="Alternativ 1") 

def b():
    return (window.update())

def sjekk_valg():
    print(f"Du valgte: {valgt_alternativ.get()}")

# 2. Lag Radiobuttons
# Legg merke til at alle har samme 'variable', men forskjellige 'value'
radio1 = ttk.Radiobutton(
    window, 
    text="Alternativ 1", 
#Basically Frame til radioknappene
    variable=valgt_alternativ, 
#Den skal sette verdien til knappen er "alternativ 1" altså valgt_anternativ blir da Alternativ 1
    value="Alternativ 1",
    command=sjekk_valg
)
radio1.pack(pady=5)

radio2 = ttk.Radiobutton(
    window, 
    text="Alternativ 2", 
    variable=valgt_alternativ, 
    value="Alternativ 2",
    command=sjekk_valg
)
radio2.pack(pady=5)

radio3 = ttk.Radiobutton(
    window, 
    text="Alternativ 3", 
    variable=valgt_alternativ, 
    value="Alternativ 3",
    command=sjekk_valg
)
radio3.pack(pady=5)


a = tk.Button(window, command = b)
a.pack()
window.mainloop()