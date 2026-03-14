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

p1 = OOP_Løsing(0, "")

#Mellomledd mellom OOP og Tkinter---------
def finn_top_spill_mellomledd():
    try:
        valgt_spill = int(finn_top_spill_entry.get())
        p1.rank = valgt_spill
        svar = p1.finn_top_spill()
        a = "\n".join(svar)
        
        if valgt_spill in df["rank"]:
            finn_top_spill_label.config(
                text = a, 
                justify= "left", 
                anchor= "nw"
            )
        else:
            finn_top_spill_label.config(text = "Skriv noe inn!")   
    except:
        finn_top_spill_label.config(text = "Skriv noe inn!") 

def finn_hours_mellomledd():
    try:
        valgt_spill = str(finn_hours_entry.get()).title()
        p1.spill = valgt_spill
        svar = p1.finn_hours()
        if valgt_spill in df["game"].values:
            finn_hours_label.config(
                text = svar, 
                justify= "left", 
                anchor= "nw"
            )
        else:
            finn_hours_label.config(text = "Skriv noe inn")
    except:
        finn_hours_label.config(text = "Skriv noe inn")

def finn_antall_spiller_mellomledd():
    try:
        valgt_spill = str(finn_antall_spiller_entry.get()).capitalize()
        p1.spill = valgt_spill
        svar = p1.finn_antall_spiller()
        if valgt_spill in df["game"].values:
            finn_antall_spiller_label.config(
                text = svar, 
                justify= "left", 
                anchor= "nw"
            )
        else:
            finn_antall_spiller_label.config(text = "Skriv noe inn")

    except:
        finn_antall_spiller_label.config(text = "Skriv noe inn")

#Tkinter del -----------------------------------------
window = ttk.Window(themename="minty")
window.title("Spill")
window.geometry("900x600")

window.columnconfigure((0,1,2), weight= 1)

font_a = tkf.Font(
        family = "Helvetica",
        size = 15
        )

tittel = ttk.Label(
        window, 
        text = "Spill", 
        font = ("Helvetica", 20)
    )
tittel.grid(
        column = 0, 
        row = 0, 
        pady = 25, 
        padx = 20, 
        columnspan= 3
)

# TOP SPILL DEL ____________________________________________________________________________________---
finn_top_spill_frame = tk.Frame(
    window, 
    padx = 10, 
    pady= 10, 
    bd  =0, 
    relief = "solid"
)
finn_top_spill_frame.grid(
    column = 0, 
    row = 1, 
    sticky= "nsew", 
    ipadx  = 50
)

finn_top_spill_label_tittel = ttk.Label(
    finn_top_spill_frame, 
    text = "Finne Top Spill", 
)
finn_top_spill_label_tittel.pack(anchor="center")

finn_top_spill_entry = ttk.Entry(
    finn_top_spill_frame 
)
finn_top_spill_entry.pack(anchor= "center")

finn_top_spill_button = ttk.Button(
    finn_top_spill_frame, 
    text = "Knapp",  
    command = finn_top_spill_mellomledd
)
finn_top_spill_button.pack(anchor="center")

finn_top_spill_label = ttk.Label(
    finn_top_spill_frame,  
    text = "Resultat her!"
)
finn_top_spill_label.pack(anchor= "center")

# ANTALL HOURS -------------------------------------------------------------------------------------
finn_hours_label_frame = tk.Frame(
    window, 
    padx = 10, 
    pady= 10, 
    bd  =0, 
    relief = "solid"
)
finn_hours_label_frame.grid(
    column= 1, 
    row = 1, 
    sticky= "nsew", 
    ipadx = 50
)


finn_hours_label_tittel = ttk.Label(
    finn_hours_label_frame, 
    text = "Antall Timer", 
)
finn_hours_label_tittel.pack(anchor= "center")

finn_hours_entry = ttk.Entry(
    finn_hours_label_frame
)   
finn_hours_entry.pack(anchor= "center")

finn_hours_button = ttk.Button(
    finn_hours_label_frame, 
    text = "Knapp", 
    command = finn_hours_mellomledd
)
finn_hours_button.pack(anchor= "center")

finn_hours_label = ttk.Label(
    finn_hours_label_frame, 
    text = "Resultat her", 
)
finn_hours_label.pack(anchor= "center")

#Antall spillere --------------------------------------------------------------------------------
finn_antall_spiller_label_frame = tk.Frame(
    window, 
    padx = 10, 
    pady= 10, 
    bd  =0, 
    relief = "solid"
)
finn_antall_spiller_label_frame.grid(
    column = 2, 
    row = 1, 
    sticky= "nsew", 
    ipadx = 50
)

finn_antall_spiller_label_tittel = ttk.Label(
    finn_antall_spiller_label_frame, 
    text = "Antall Spillere", 
)
finn_antall_spiller_label_tittel.pack(anchor= "center")

finn_antall_spiller_entry = ttk.Entry(
    finn_antall_spiller_label_frame)
finn_antall_spiller_entry.pack(anchor= "center")

finn_antall_spiller_Button = ttk.Button(
    finn_antall_spiller_label_frame, 
    text = "Knapp", 
    command = finn_antall_spiller_mellomledd
)
finn_antall_spiller_Button.pack(anchor= "center")

finn_antall_spiller_label = ttk.Label(
    finn_antall_spiller_label_frame, 
    text = "Resultat her", 
)
finn_antall_spiller_label.pack(anchor= "center")

window.mainloop()