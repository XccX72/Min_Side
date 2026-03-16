from datetime import datetime, UTC, timedelta
import ttkbootstrap as ttk
import pandas as pd
import os
import time

#-----------------------------------------------------------------------------
#Pandas
#-----------------------------------------------------------------------------
# Finn mappen der dette scriptet ligger

denne_mappen = os.path.dirname(__file__)

# Gå ett hakk OPP (..), og så inn i csv_filer
filsti = os.path.join(denne_mappen, "csv_filer", "land_tidssoner.csv")

df = pd.read_csv(filsti)

#-----------------------------------------------------------------------------
#Funksjoner
#-----------------------------------------------------------------------------
#Norge tid og dato ----------------------------------------
def norges_tid():
    nå = datetime.now()
    nå_klokkeslett = nå.strftime("%H:%M:%S")
    tidssone_Norge_tid.config(text = nå_klokkeslett)
    #after er tkinter metode for basically å vente med noe målt i millie sek
    tidssone_Norge_tid.after(1000, norges_tid)

def norges_dato():
    nå = datetime.now()
    nå_dato = nå.strftime("%d.%m.%Y")
    Dato_Norge_label.config(text = nå_dato)
    i_morgen = nå + timedelta(days = 1)
    neste_midnatt = datetime(
        year=i_morgen.year, 
        month=i_morgen.month, 
        day=i_morgen.day, 
        hour=0, minute=0, second=1
    )
    ventetid_ms = int((neste_midnatt - nå).total_seconds()*1000)

    Dato_Norge_label.after(ventetid_ms, norges_dato)

  # Valgtfrisone deler -----------------------------------------------------------------------------------  
def valgfrisone_1():
    try:
        land_valgt = valgfrisone1_combobox.get().strip()
        land_valgt_df = df.loc[df["Land"].str.strip() == land_valgt, "offset"]
        if not land_valgt_df.empty:
            utc_tid = datetime.now(UTC)

            offset_tid = float(land_valgt_df.values[0])
            sone_tid = utc_tid + timedelta(hours = offset_tid)

            klokkeslett = sone_tid.strftime("%H.%M.%S")
            valgfrisone1_label.config(text = klokkeslett)
            valgfrisone1_label.after(1000, valgfrisone_1)
    except:
        valgfrisone1_label.config(text = "Choose Country")

def valgfrisone_2():
    try:
        land_valgt = valgfrisone2_combobox.get().strip()
        land_valgt_df = df.loc[df["Land"].str.strip() == land_valgt, "offset"]
        if not land_valgt_df.empty:
            utc_tid = datetime.now(UTC)

            offset_tid = float(land_valgt_df.values[0])
            sone_tid = utc_tid + timedelta(hours = offset_tid)

            klokkeslett = sone_tid.strftime("%H.%M.%S")
            valgfrisone2_label.config(text = klokkeslett)
            valgfrisone2_label.after(1000, valgfrisone_2)
    except:
        valgfrisone2_label.config(text = "Choose Country")

#Stoppeklokke ------------------------------------------------------
start = 0
kjører = False

def stoppeklokke_oppdater():
    global start, kjører
    if kjører:
        nå = time.perf_counter() - start
        Stoppeklokke_label.config(text = f"{nå:.2f} Sec")
        Stoppeklokke_label.after(50, stoppeklokke_oppdater)

def stoppeklokke_start():   
    global kjører, start
    if not kjører:
        start = time.perf_counter()
        kjører = True
        stoppeklokke_oppdater()
        

def stoppeklokke_ferdig():
    global kjører
    kjører = False

def stoppeklokke_nullstill():
    global start, kjører
    kjører = False
    start = 0
    Stoppeklokke_label.config(text = "0.00 Sec" )

#------------------------------------------------------------------------------
#Tkinter
#----------------------------------------------------------------------------
def tkinter_del_time_main(vindu):
    global valgfrisone1_button, valgfrisone2_button, valgfrisone1_combobox, valgfrisone2_combobox, content_frame, tidssone_Norge_tid, valgfrisone1_label, valgfrisone2_label, Dato_Norge_label, Stoppeklokke_label
    content_frame = vindu

    # For tidssone delen ------------------------------------------------------    
    tidssone_frame = ttk.Frame(
        content_frame
    )
    tidssone_frame.grid(
        column = 0,
        row = 0, 
        columnspan= 2
    )
    #Norge del ---------------------------------
    tidssone_Norge_label = ttk.Label(
        tidssone_frame,
        text = "Norway Time"
    )
    tidssone_Norge_label.grid(
        column= 0, 
        row = 0,
        rowspan= 2, 
        columnspan= 3
    )
    tidssone_Norge_tid = ttk.Label(
        tidssone_frame,
        text = "Norway's Time",
    )
    tidssone_Norge_tid.grid(
        column= 0,
        row=1,
        rowspan=2,
        columnspan= 3
    )
    #Valgfri sone 1 --------------------
    #Hva vi kan velge mellom
    elementlist = df["Land"].tolist()

    valgfrisone1_combobox = ttk.Combobox(
        tidssone_frame,
        state = "readonly", #"normal" skriv og velge "writeonly" er kun skriving
        values = elementlist
    )
    valgfrisone1_combobox.grid(
        columnspan= 2,
        column= 3,
        row = 0
    )
    valgfrisone1_button = ttk.Button(
        tidssone_frame,
        text = "Perform",
        command = valgfrisone_1
    )
    valgfrisone1_button.grid(
        column = 5,
        row  = 0 
    )
    valgfrisone1_label = ttk.Label(
        tidssone_frame,
        text = "Time Zone"
    )
    valgfrisone1_label.grid(
        column=3,
        row = 1,
        columnspan= 3
    )

    #Valgfri sone 2 --------------------
    valgfrisone2_combobox = ttk.Combobox(
        tidssone_frame,
        state = "readonly",
        values= elementlist
    )
    valgfrisone2_combobox.grid(
        columnspan= 2,
        column= 3,
        row = 2
    )
    valgfrisone2_button = ttk.Button(
        tidssone_frame,
        text = "Perform",
        command = valgfrisone_2
    )
    valgfrisone2_button.grid(
        column = 5,
        row  = 2
    )
    valgfrisone2_label = ttk.Label(
        tidssone_frame,
        text = "Time Zone"
    )
    valgfrisone2_label.grid(
        column=3,
        row = 3,
        columnspan = 3
    )

    # Dato del ----------------------------------------------------------
    Dato_Frame = ttk.Frame(
        content_frame
    )
    Dato_Frame.grid(
        column = 0, 
        row = 1
    )

    #Dato Norge
    Dato_Norge_label = ttk.Label(
        Dato_Frame,
        text = "Norway Dato"
    ) 
    Dato_Norge_label.grid(
        column= 0,
        row = 0
    )

    # Stoppeklokke del------------------------------------------------------
    Stoppeklokke_Frame = ttk.Frame(
        content_frame
    )
    Stoppeklokke_Frame.grid(
        column = 1, 
        row = 1
    )

    #Label info
    Stoppeklokke_Label_info = ttk.Label(
        Stoppeklokke_Frame,
        text = "Stop Watch"
    )
    Stoppeklokke_Label_info.grid(
        column = 0,
        row = 0, 
        columnspan= 2
    )

    #Start knapp
    Stoppeklokke_Start_Button = ttk.Button(
        Stoppeklokke_Frame,
        command = stoppeklokke_start,
        text = "Start"
    )
    Stoppeklokke_Start_Button.grid(
        column = 2,
        row = 0
    )

    #Ferdig knapp
    Stoppeklokke_Ferdig_Button = ttk.Button(
        Stoppeklokke_Frame,
        command= stoppeklokke_ferdig,
        text = "Finish"
    )
    Stoppeklokke_Ferdig_Button.grid(
        column = 3,
        row = 0
    )

    #Nullstill knapp
    Stoppeklokke_Nullstill_Button = ttk.Button(
        Stoppeklokke_Frame,
        command = stoppeklokke_nullstill,
        text = "Reset"
    )
    Stoppeklokke_Nullstill_Button.grid(
        column = 4,
        row = 0
    )

    Stoppeklokke_label = ttk.Label(
        Stoppeklokke_Frame,
        text = "Stop Watch Results"
    )
    Stoppeklokke_label.grid(
        columnspan= 5,
        column = 0,
        row = 1
    )

    norges_tid()
    norges_dato()


