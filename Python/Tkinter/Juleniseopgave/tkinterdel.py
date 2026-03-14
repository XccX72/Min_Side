import tkinter as tk
import ttkbootstrap as ttk
import pandas as pd
import random as rnd

#bruk tk.Treeview for å bruke treeview funksjoner

df = pd.read_csv("Tkinter/Juleniseopgave/jul_barn_2000.csv")

def AddPlaceholder(entry, text):
   entry.insert(0, text)
   entry.config(foreground='grey')


   entry.bind("<FocusIn>", lambda e: entry.delete(0, tk.END) if entry.get() == text else None)
   entry.bind("<FocusOut>", lambda e: entry.insert(0, text) if entry.get() == "" else None)


def hent_navn():
    fn = fornavn_var.get().strip().lower()

    ln = etternavn_var.get().strip().lower()

    person = df[(df["fornavn"].str.lower() == fn) & (df["etternavn"].str.lower() == ln)]

    if not person.empty:
        resultat_df = person[["snillhet", "gave", "nissehjelper", "dato"]]
        resultat = resultat_df.to_string(index=False)

    else:
        resultat = "Person ikke funnet"
    
    label_navn.config(text = resultat)
    
def random_navn():
    index_number = rnd.randint(1, 2000)

    resultat_df = df.loc[index_number, ["snillhet", "gave", "nissehjelper", "dato"]]
    
    resultat =resultat_df.to_string(index=False)
    
    label_navn.config(text = resultat)

#Window
window = ttk.Window(themename= "morph")
window.title("dfdfd")
window.geometry("500x500")


fornavn_var = ttk.StringVar()
etternavn_var = ttk.StringVar()

fornavn = ttk.Entry(window, textvariable= fornavn_var)
fornavn.insert(0, "Fornavn")
fornavn.pack()

etternavn = ttk.Entry(window, textvariable= etternavn_var)
etternavn.insert(0, "Etternavn")
etternavn.pack( )

label_navn =ttk.Label(
    window,
    text = "Søk etter Person",
    font = "Nunito 13"
)
label_navn.pack()

random_navn_label = tk.Button(
    window,
    text = "Random Person",
    command = random_navn,
    font = "Nunito 13"
)
random_navn_label.pack()


tk.Button(
    window, 
    text = "Søk",
    command = hent_navn, 
    font = "Nunito 13"
).pack()

#Treeview del av window



window.mainloop()