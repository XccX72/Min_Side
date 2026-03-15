from datetime import datetime, UTC, timedelta
import ttkbootstrap as ttk
from zoneinfo import ZoneInfo, available_timezones
import pandas as pd
import os
import time

#-----------------------------------------------------------------------------
#Pandas
#-----------------------------------------------------------------------------
# Finn mappen der dette scriptet ligger

denne_mappen = os.path.dirname(__file__)

# Gå ett hakk OPP (..), og så inn i csv_filer
filsti = os.path.abspath(os.path.join(denne_mappen,  "land_tidssoner.csv"))

df = pd.read_csv(filsti)

#-----------------------------------------------------------------------------
#Funksjoner
#-----------------------------------------------------------------------------

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
    
def valgfrisone_1():
    try:
        land_valgt = valgfrisone1_combobox.get()
        land_valgt_df = df.loc[df["Land"] == land_valgt, "UTC offset"].values[0]
        if not land_valgt_df.empty:
            utc_tid = datetime.now(UTC)
            sone_tid = utc_tid + timedelta(hours = int(land_valgt_df))
            klokkeslett = sone_tid.strftime("%H.%M.%S")
            valgfrisone1_label.config(text = klokkeslett)
            valgfrisone1_label.after(1000, valgfrisone_1)
    except:
        valgfrisone1_label.config(text = "Choose Country")
        


def valgfrisone_2():
    pass

def stoppeklokke_start():
    pass

def stoppeklokke_ferdig():
    pass

def stoppeklokke_nullstill():
    pass

def keys(event):
    global lås
    key = event.keysym

    if key == "Escape":
        content_frame.destroy()
    else:
        return

#------------------------------------------------------------------------------
#Tkinter
#----------------------------------------------------------------------------
def tkinter_del_time_main():
    global valgfrisone1_button, valgfrisone2_button, valgfrisone1_combobox, valgfrisone2_combobox, content_frame, tidssone_Norge_tid, valgfrisone1_label, valgfrisone2_label, Dato_Norge_label, Stoppeklokke_label
    content_frame = ttk.Window(themename= "minty")
    content_frame.state("zoomed")

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
        state = "normal",
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
        state = "normal",
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
    content_frame.bind_all("<KeyPress>", keys)
    content_frame.mainloop()


if __name__ == "__main__":
    tkinter_del_time_main()
