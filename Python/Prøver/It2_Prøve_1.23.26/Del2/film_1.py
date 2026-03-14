import pandas as pd
import tkinter as tk
import ttkbootstrap as ttk
from PIL import Image, ImageTk
import os

aaaaaa = os.path.dirname(__file__)
filsti = os.path.join(aaaaaa, "imdb_top250.csv")
df = pd.read_csv(filsti)

df.info()

class analysre_data:
    def __init__(self, film_valgt, regissør_valgt, rank):
        self.film_valgt = film_valgt
        self.regissør_valgt = regissør_valgt
        self.rank = rank

    def finn_rangering(self):
        bf = df[df["rangering"] <= self.rank]
        c = bf["tittel"].tolist()
        return c
    
    def finn_min(self):
        aaa = df[df["tittel"] == self.film_valgt]
        b = aaa["varighet_min"].sum()
        return (f"Antall min: {b}")

def hent_rank_mellomledd():
    try:
        valgt_spill = int(finn_top_spill_entry.get())
        p1.rank = valgt_spill
        svar = p1.finn_rangering()
        a = "\n".join(svar)
        if valgt_spill in df["rangering"]:
            finn_top_spill_label.config(
                text = a, 
                justify= "left", 
                anchor= "nw"
            )
        else:
            finn_top_spill_label.config(text = "Skriv noe inn")
    except:
        finn_top_spill_label.config(text = "Skriv noe inn")

def finn_hours_mellomledd():
    try:
        valgt_spill = str(finn_hours_entry.get()).title()
        p1.film_valgt = valgt_spill
        svar = p1.finn_min()
        if valgt_spill in df["tittel"].values:
            finn_hours_label.config(
                text = svar, 
                justify= "left", 
                anchor= "nw"
            )
        else:
            finn_hours_label.config(text = "Skriv noe inn")
    except:
        finn_hours_label.config(text = "Skriv noe inn")


p1 = analysre_data("", "", 0)

window = ttk.Window(themename= "minty")
window.geometry("1250x700")
window.title("Analysering")

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
finn_top_spill_label_forklaring = ttk.Label(
    finn_top_spill_frame, 
    text = "Skriv tall"
)
finn_top_spill_label_forklaring.pack(anchor= "center")
finn_top_spill_label_tittel.pack(anchor="center")

finn_top_spill_entry = ttk.Entry(
    finn_top_spill_frame 
)
finn_top_spill_entry.pack(anchor= "center")

finn_top_spill_button = ttk.Button(
    finn_top_spill_frame, 
    text = "Knapp",  
    command = hent_rank_mellomledd
)
finn_top_spill_button.pack(anchor="center")

finn_top_spill_label = ttk.Label(
    finn_top_spill_frame,  
    text = "Resultat her!"
)
finn_top_spill_label.pack(anchor= "center")

#2 metode -----------------------------
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

bilde = Image.open("film_ruller.webp")
bilde_bla = ImageTk.PhotoImage(bilde)

a = tk.Label(
    window, image = bilde_bla
)
a.grid(column = 3, row = 1, columnspan= 2)

window.mainloop()