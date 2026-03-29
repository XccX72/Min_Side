import ttkbootstrap as ttk
import Sub_Pages.mol_kalkulator_v3 as mol_calc
import Sub_Pages.time_v1 as time_file
import Sub_Pages.informasjons_del_v1 as info_file
import Sub_Pages.text as txt

window = ttk.Window(themename= "minty")
window.state("zoomed")
window.title("Homepage")
window.grid_columnconfigure(1, weight=1)
window.grid_rowconfigure(1, weight=1)

#-----------------------------------------------------
#Funksjoner om knapper
#-----------------------------------------------------
#Fjerne allerede lagde widgets
def clear_content():
    for widget in content_frame.winfo_children():
        widget.destroy()

#For om csv leser
def proff(): #For informasjons knappen
    clear_content()
    info_file.tkinter_del(content_frame)

def klokke(): #For Time knappen
    clear_content()
    time_file.tkinter_del_time_main(content_frame)
    
#About me fane
def about_me():
    clear_content()
    txt.info_om_meg(content_frame)

def about_me_viktig():
    clear_content()
    txt.viktig_om_meg(content_frame)

#Help Keys Fane
def help_keys():
    clear_content()
    txt.keys_info(content_frame)


def mol_kalkulator():
    clear_content()
    mol_calc.tkinter_del(content_frame)

#-----------------------------------------------------
#Meny
#-----------------------------------------------------
lås = False

#Oppretter Meny
def meny():
    global lås, meny_frame
    if lås == False:
        meny_frame.grid()
        window.focus_force()
        lås = True
    elif lås == True:
        if meny_frame:
            meny_frame.grid_remove()
        lås = False

#--------------------------------------------------------
#Meny Frame
meny_frame = ttk.Frame(
    window
)
meny_frame.grid(
    column= 0, 
    row = 1, 
    sticky= "n"
)

#About_me knapp
meny_about_me_button = ttk.Button(
    meny_frame, 
    text = "Om Meg (Hobbies etc)", 
    command= about_me, 
    width= 33
)
meny_about_me_button.pack(
    fill = "x", 
    ipady = 20
)
meny_viktig_me_button = ttk.Button(
    meny_frame, 
    text = "Viktig om meg(CV etc)",
    command= about_me_viktig,
    width= 33
)
meny_viktig_me_button.pack(
    fill= "x",
    ipady = 20
)

#Hjelp_knapper knapp
meny_help_knapper_button = ttk.Button(
    meny_frame, 
    command = help_keys,
    width= 33, 
    text = "Help Keys"
    )
meny_help_knapper_button.pack(
    fill= "x",
    ipady = 20
)

#Mol_kalkulator Knapp
meny_mol_kalkulator_button = ttk.Button(
    meny_frame, 
    command= mol_kalkulator, 
    width= 33, 
    text = "Mol Calc"
)
meny_mol_kalkulator_button.pack(
    fill= "x",
    ipady = 20
)

meny_time_button = ttk.Button(
    meny_frame, 
    text = "Time", 
    command = klokke,
    width= 33
)
meny_time_button.pack(
    fill= "x",
    ipady = 20
)
proff_knapp = ttk.Button(
    meny_frame, 
    text = "CSV Leser", 
    command= proff, 
    width= 33
)
proff_knapp.pack( 
    fill= "x",
    ipady = 20
)
#-------------------------------------------------
#Meny knapp
#-------------------------------------------------
meny_åpne = ttk.Button(
    window,
    text= "Meny", 
    command = meny, 
    width= 33
)
meny_åpne.grid(
    row = 0, 
    column= 0, 
    sticky= "nw", 
    ipady= 20, 
)

#----------------------------------------------------
#Backend Frame
#----------------------------------------------------
content_frame = ttk.Frame(
    window
)
content_frame.grid(
    row = 0,
    column= 1, 
    rowspan= 2,
    sticky= "nwes"
)

#-----------------------------------------------------
#Keys
#-----------------------------------------------------
def keys(event):
    global lås
    key = event.keysym

    if key == "Escape":
        window.destroy()
    if key.lower() == "m":
        meny()
    else:
        return
    """
    elif key == "1" and lås == True:
        about_me()
    elif key == "2" and lås == True:
        proff()
    elif key == "3" and lås == True:
        help_keys()
    elif key == "4" and lås == True:
        mol_kalkulator()
    """
window.bind_all("<KeyPress>", keys)
window.focus_force()
window.mainloop()