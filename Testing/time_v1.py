from datetime import datetime, UTC
import ttkbootstrap as ttk
from zoneinfo import ZoneInfo, available_timezones
import pandas as pd
import os

#-----------------------------------------------------------------------------
#Pandas
#-----------------------------------------------------------------------------
# Finn mappen der dette scriptet ligger

"""denne_mappen = os.path.dirname(__file__)

# Gå ett hakk OPP (..), og så inn i csv_filer
filsti = os.path.abspath(os.path.join(denne_mappen, "..", "csv_filer", "land_tidssoner.csv"))

df = pd.read_csv(filsti)"""

#-----------------------------------------------------------------------------
#Funksjoner
#-----------------------------------------------------------------------------
def valgfrisone_1():
    pass

def valgfrisone_2():
    pass

def stoppeklokke_start():
    pass

def stoppeklokke_ferdig():
    pass

def stoppeklokke_nullstill():
    pass


#------------------------------------------------------------------------------
#Tkinter
#----------------------------------------------------------------------------
def tkinter_del_time():
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
    #elementlist = df["Land"].tolist

    valgfrisone1_combobox = ttk.Combobox(
        tidssone_frame,
        state = "normal"
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
        state = "normal"
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

    content_frame.mainloop()


tkinter_del_time()
