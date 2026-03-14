import ttkbootstrap as ttk
import pandas as pd
import os

#----------------------------------------------------------
#Pandas Filsti
#----------------------------------------------------------
mappe = os.path.dirname(__file__)
filsti = os.path.join(mappe,"csv_filer", "grunnstoffer.csv")
df = pd.read_csv(filsti)

#-----------------------------------------------------------
#Funksjoner
#-----------------------------------------------------------
mol = 6.022e23

def beregner_partikkler():
    #antall partikler for i mol
    i = float(skrive.get())
    p = mol * i
    resultat_label.config(text= f"Partikler = {p :.2e}")

def beregn_mol():
    # antall mol for i partikler
    i = float(skrive.get())
    m = i/mol
    resultat_label.config(text = f"Mol = {m:.4f}")

def hvilket_grunnstoff():
    i = int(info_entry.get())
    resultat = df[df['Atomnummer'] == i]

    if not resultat.empty:
        navn = resultat['Navn'].values[0]
        masse = resultat['Molarmasse'].values[0]
        symbol = resultat['Symbol'].values[0]
        Elektronegativitet = resultat['Elektronegativitet'].values[0]
        info_text = (f"Navn: {navn}\nSymbol : {symbol} \nMolarMasse : {masse}\nElektronegativitet : {Elektronegativitet}")
        info_Label.config(text = info_text)    
    else:
        info_Label.config(text = f"Fant ikke atomnummeret :(")

def finn_gram():
    try: 
        Valgt_element = (hvilken_funksjon.get())
        antall_mol = float(hvilket_grunnstoff_funksjoner.get())
        rad = df[df["Navn"] == Valgt_element]
        molar_masse = rad["Molarmasse"].values[0]
        gram = antall_mol * molar_masse
        if not rad.empty:
            hvilken_funksjon_label.config(text = f"Antall gram: {gram}") 
        else:
            hvilken_funksjon_label.config(text = "Velg et grunnstoff!")
    except ValueError:
        hvilken_funksjon_label.config(text = "Skriv inn noe!!")

def finn_mol():
    try:
        Valgt_element = hvilken_funksjon.get()
        antall_gram = float(hvilket_grunnstoff_funksjoner.get())
        rad = df[df["Navn"] == Valgt_element]
        if not rad.empty:
            molar_masse = rad["Molarmasse"].values[0]
            mol1 = antall_gram / molar_masse
            hvilken_funksjon_label.config(text = f"Antall Mol: {mol1}")
        else: 
            hvilken_funksjon_label.config(text = "Skriv inn noe!!")
    except ValueError:
        hvilken_funksjon_label.config(text= "Skriv inn noe!!")

def finn_liter():
    try:
        antall_mol = float(konsentrasjon_entry_antall_mol.get())
        konsentrasjon = float(konsentrasjon_entry_hvilken_konsentrasjon.get())
        if konsentrasjon == 0:
            konsentrasjon_label.config(text= f"Skriv noe inn!!")
        svar = antall_mol / konsentrasjon
        konsentrasjon_label.config(text = f"Trenger {svar} L")
    except:
        konsentrasjon_label.config(text = "Skriv noe!!")

def konsentrasjon_finn_mol():
    try:
        antall_liter = float(konsentrasjon_entry_antall_mol.get())
        konsentrasjon = float(konsentrasjon_entry_hvilken_konsentrasjon.get())
        if konsentrasjon == 0:
            konsentrasjon_label.config(text = "Skriv noe!!")
        svar = konsentrasjon* antall_liter
        konsentrasjon_label.config(text = f"Trenger {svar} Mol")

    except:
        konsentrasjon_label.config(text = "Skriv noe!!")
#--------------------------------------------------------------
#Tkinter
#--------------------------------------------------------------

def tkinter_del(hoved_vindu):
    global skrive, resultat_label, info_entry, info_Label, hvilken_funksjon, hvilket_grunnstoff_funksjoner, konsentrasjon_label, content_frame, hvilken_funksjon_label, konsentrasjon_entry_hvilken_konsentrasjon, konsentrasjon_entry_antall_mol
    content_frame = hoved_vindu
        #Partikler/Mol del (Andre Kvadrant) ------------------------------------------------------------

    # Funksjonenen  partikkler
    partikkler_label_info = ttk.Label(
        content_frame,
        text = "Mol = Partikler"
    )
    partikkler_label_info.grid(
        column = 0, 
        row = 0, 
        padx = 10,
        pady = 10,
        ipadx = 15, 
        ipady= 10, 
        columnspan= 2
    )

    skrive = ttk.Entry(
        content_frame
    )
    skrive.grid(
        column = 0,
        row = 1,
        padx = 10,
        pady = 10,
        columnspan= 2
    )

    partikkler_knapp = ttk.Button(
        content_frame,
        text = "Partikkel Beregner",
        command = beregner_partikkler
        )
    partikkler_knapp.grid(
        column = 0,
        row = 2,
        padx = 10,
        pady = 10,
        ipadx = 15, 
        ipady= 10
    )
    # Funksjonenen  mol

    mol_knapp = ttk.Button(
        content_frame,
        text = "Mol",
        command = beregn_mol
    )
    mol_knapp.grid(
        column = 1,
        row = 2,
        padx = 10,
        pady = 10,
        ipadx = 25, 
        ipady= 10
    )

    resultat_label = ttk.Label(
        content_frame, 
        text="Resultat vises her: Partikler/Mol",
        )
    resultat_label.grid(
        column=0, 
        row=3, 
        columnspan=2, 
        pady=10
    )

    # grunnstoff info (Første kvadrant)---------------------------------------------------------------------------------------------------
    grunnstoff_label = ttk.Label(
        content_frame,
        text = "Info Grunnstoff\n1 - 118"
    )
    grunnstoff_label.grid(
        column= 2, 
        row=0,
        padx = 10,
        pady = 10,
        ipadx = 15, 
        ipady= 10, 
        columnspan= 2
    )

    grunnstoff = ttk.Button(
        content_frame, 
        text = "Mol", 
        command = hvilket_grunnstoff
    )
    grunnstoff.grid(
        column = 2,
        row = 2, 
        pady = 10, 
        padx = 10, 
        ipadx = 25, 
        ipady = 10, 
        columnspan= 2
    )

    info_entry = ttk.Entry(
        content_frame
        )
    info_entry.grid(
        column = 2, 
        row = 1, 
        pady = 10, 
        padx = 10, 
        columnspan= 2
    )
    info_Label = ttk.Label(
        content_frame, 
        text="Resultat vises her: Grunnstoff Info"
    )
    info_Label.grid(
        column = 2, 
        row = 3, 
        pady = 10, 
        padx = 10, 
        columnspan= 2
    )

    # Gram/antall mol beregner (Tredre kvadrant---------------------------------------------------------------------------------------------
    #For å finne gram eller antall mol ved hjelp av molarmasse
    #.tolist() omgjør en kolonne til en liste [], for eksempel game kolonne blir til ["Minecraft", "Fortnite"]
    elementliste = df["Navn"].tolist()
    #element

    hvilken_funksjon_label_info = ttk.Label(
        content_frame,
        text = "Antall Gram/Mol"
    )
    hvilken_funksjon_label_info.grid(
        row = 4, 
        column= 0, 
        columnspan= 2,
        padx = 10,
        pady = 10,
        ipadx = 15, 
        ipady= 10
    )

    hvilken_funksjon = ttk.Combobox(
        content_frame, 
        values=elementliste, 
    )
    hvilken_funksjon.grid(
        column= 0,
        row = 5, 
        pady = (10,), 
        padx = (10, 0)
    )

    hvilket_grunnstoff_funksjoner = ttk.Entry(
        content_frame, 
    )
    hvilket_grunnstoff_funksjoner.grid(
        padx = (0, 10),
        pady = (10), 
        column = 1,
        row = 5
    )

    hvilken_funksjon_Button = ttk.Button(
        content_frame, 
        command = finn_gram, 
        text = "Gram Beregner"
    )
    hvilken_funksjon_Button.grid(
        column = 0, 
        row = 6, 
        pady = 10, 
        padx = 10, 
        ipadx = 25, 
        ipady = 10
    )
    hvilken_funksjon_Button1 = ttk.Button(
        content_frame, 
        command = finn_mol, 
        text = "Antall Mol Beregner"
    )
    hvilken_funksjon_Button1.grid(
        column = 1, 
        row = 6, 
        ipadx = 25, 
        ipady = 10, 
        padx = 10, 
        pady = 10
    )

    hvilken_funksjon_label = ttk.Label(
        content_frame, 
        text = "Resultat Her"
    )
    hvilken_funksjon_label.grid(
        column= 0, 
        row = 7, 
        pady = 10, 
        padx = 10, 
        columnspan= 2
    )

    # Konsentrasjon Beregning (Fjerde Kvadrant)------------------------------------------------------------------------------------------
    # hvilken konsentrasjon hvis du vet antall mol

    konsentrasjon_label_info = ttk.Label(
        content_frame, 
        text = "Konsentrasjon\nL/Mol / M(Mol/L)"
    )
    konsentrasjon_label_info.grid(
        columnspan= 2, 
        column=2, 
        row = 4, 
        padx = 10,
        pady = 10,
        ipadx = 15, 
        ipady= 10
    )

    konsentrasjon_entry_antall_mol = ttk.Entry(
        content_frame
    )
    konsentrasjon_entry_antall_mol.grid(
        column = 2, 
        row = 5, 
        pady = 10, 
        padx = (10, 0)
    )
    konsentrasjon_entry_hvilken_konsentrasjon = ttk.Entry(
        content_frame
    )
    konsentrasjon_entry_hvilken_konsentrasjon.grid(
        column = 3, 
        row = 5, 
        pady = 10, 
        padx  = (0, 10) 
    )
    konsentrasjon_Button_finn_liter = ttk.Button(
        content_frame,  
        command = finn_liter,
        text = "Liter Beregner"
    )
    konsentrasjon_Button_finn_liter.grid(
        column = 2, 
        row = 6, 
        ipadx = 25, 
        ipady = 10, 
        pady = 10, 
        padx = 10
    )
    konsentrasjon_Button_finn_mol = ttk.Button(
        content_frame, 
        command = konsentrasjon_finn_mol,
        text = "Mol Beregner"
    )
    konsentrasjon_Button_finn_mol.grid(
        column = 3, 
        row = 6, 
        ipadx = 25, 
        ipady = 10, 
        pady = 10, 
        padx = 10
    )

    konsentrasjon_label = ttk.Label(
        content_frame,  
        text = "Resultat her"
    )
    konsentrasjon_label.grid(
        column = 2, 
        row = 7, 
        ipadx = 25, 
        ipady = 10, 
        padx= 10, 
        pady  =10, 
        columnspan= 2
    )

if __name__ == "__main__":
    tkinter_del()