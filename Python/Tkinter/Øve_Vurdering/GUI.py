import tkinter as tk
import pandas as pd
import ttkbootstrap as ttk
import tkinter.font as tkf

#Tkinter/Øve_Vurdering/
df = pd.read_csv("Tkinter/Øve_Vurdering/ps5_top100.csv")

#OOP del .--------------------------------------------------
class OOP_Løsing:
    def __init__(self, rank:int, spill:str):
        self.rank = rank
        self.spill = spill

    def finn_top_spill(self):
        bf = df[df["rank"] <= self.rank]
        c = bf["game"].tolist()
        return c
    
    def finn_antall_spiller(self):
        a = df[df["game"] == self.spill]
        b = a["players"].sum()
        return (f"Antall spillere: \n{b}")

    def finn_hours(self):
        a = df[df["game"] == self.spill]
        b = a["hours_played"].sum()
        return(f"Antall timer: \n{b}") 

p1 = OOP_Løsing(1, "")

#Mellomledd mellom OOP og Tkinter---------
def finn_top_spill_mellomledd():
    valgt_spill = int(finn_top_spill_entry.get())
    p1.rank = valgt_spill
    svar = p1.finn_top_spill()
    a = "\n".join(svar)
    
    finn_top_spill_label.config(
        text = a, 
        justify= "left", 
        anchor= "nw"
    )

def finn_hours_mellomledd():
    valgt_spill = str(finn_hours_entry.get()).capitalize()
    svar = p1.finn_hours()
    p1.spill = valgt_spill
    finn_hours_label.config(
        text = svar, 
        justify= "left", 
        anchor= "nw"
    )

def finn_antall_spiller_mellomledd():
    valgt_spill = str(finn_antall_spiller_entry.get()).capitalize()
    svar = p1.finn_antall_spiller()
    p1.spill = valgt_spill
    finn_antall_spiller_label.config(
        text = svar, 
        justify= "left", 
        anchor= "nw"
    )

#Tkinter del -----------------------------------------
window = ttk.Window(themename="minty")
window.title("Spill")
window.geometry("750x500")

font_a = tkf.Font(
        family = "Helvetica",
        size = 15
        )

tittel = ttk.Label(
        window, 
        text = "Spill", 
    )
tittel.grid(
        column = 0, 
        row = 0, 
        pady = 25, 
        padx = 20, 
        columnspan= 2
)

# TOP SPILL DEL ____________________________________________________________________________________---
finn_top_spill_label_tittel = ttk.Label(
    window, 
    text = "Finne Top Spill", 
)
finn_top_spill_label_tittel.grid(
    column = 0, 
    row = 1, 
    pady = 10, 
    padx  = 20
)
finn_top_spill_entry = ttk.Entry(
    window, 
)
finn_top_spill_entry.grid(
    column = 0, 
    row = 2, 
    pady = 10, 
    padx = 20
)
finn_top_spill_button = ttk.Button(
    window, 
    text = "Knapp",  
    command = finn_top_spill_mellomledd
)
finn_top_spill_button.grid(
    column = 0, 
    row = 3, 
    pady = 10, 
    padx  = 20
)
finn_top_spill_label = ttk.Label(
    window,  
    text = "Resultat her!"
)
finn_top_spill_label.grid(
    column = 0, 
    row = 4, 
    pady  = 10, 
    padx  = 20
)

# ANTALL HOURS -------------------------------------------------------------------------------------
finn_hours_label_tittel = ttk.Label(
    window, 
    text = "Antall Timer", 
)
finn_hours_label_tittel.grid(
    column = 1, 
    row = 1, 
    pady = 10, 
    padx = 20
)
finn_hours_entry = ttk.Entry(
    window,
)   
finn_hours_entry.grid(
    column= 1, 
    row = 2, 
    padx = 20, 
    pady = 10
)
finn_hours_button = ttk.Button(
    window, 
    text = "Knapp", 
    command = finn_hours_mellomledd
)
finn_hours_button.grid(
    column = 1, 
    row = 3, 
    padx = 20, 
    pady = 10
)
finn_hours_label = ttk.Label(
    window, 
    text = "Resultat her", 
)
finn_hours_label.grid(
    column = 1, 
    row = 4,
    pady = 10, 
    padx  = 20
)

#Antall spillere --------------------------------------------------------------------------------
finn_antall_spiller_label_tittel = ttk.Label(
    window, 
    text = "Antall Spillere", 
)
finn_antall_spiller_label_tittel.grid(
    column = 2, 
    row = 1, 
    padx = 20,
    pady = 10
)
finn_antall_spiller_entry = ttk.Entry(
    window, 

)
finn_antall_spiller_entry.grid(
    column= 2, 
    row = 2, 
    pady = 10, 
    padx = 20
)
finn_antall_spiller_Button = ttk.Button(
    window, 
    text = "Knapp", 
    command = finn_antall_spiller_mellomledd
)
finn_antall_spiller_Button.grid(
    column = 2, 
    row = 3, 
    padx = 20, 
    pady = 10
)
finn_antall_spiller_label = ttk.Label(
    window, 
    text = "Resultat her", 
)
finn_antall_spiller_label.grid(
    column = 2, 
    row = 4, 
    padx = 20, 
    pady = 10
)
window.mainloop()