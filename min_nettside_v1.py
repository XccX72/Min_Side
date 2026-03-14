import ttkbootstrap as ttk
import mol_kalkulator_v3

window = ttk.Window(themename= "minty")
window.state("zoomed")
window.title("Homepage")
window.grid_columnconfigure(1, weight=1)
window.grid_rowconfigure(1, weight=1)

#-----------------------------------------------------
#Funksjoner
#-----------------------------------------------------

#Fjerne allerede lagde widgets
def clear_content():
    for widget in content_frame.winfo_children():
        widget.destroy()

#proff delen
def proff():
    pass



#About me fane
def about_me():
    clear_content()
    about_me_label_h1 = ttk.Label(
        content_frame, 
        text = "Hello", 
        font= ("Arial", 20)
    )
    about_me_label_h1.pack()

    about_me_label_t1 = ttk.Label(
        content_frame,
        text = "Hi, \nMy name is Danni Spriet and I am a 'programmer'. \nI'm studying programming via my high school, Olsvikåsen VGS ",
        font = ("Arial", 12)
    )
    about_me_label_t1.pack()

#Help Keys Fane
def help_keys():
    clear_content()
    help_keys_label = ttk.Label(
        content_frame, 
        text = "M = Meny \nEsc = Close Program \nAbout Me = 1\nInformation = 2\nHelp Keys = 3\nMol Calc = 4", 
        font= ("Arial", 20)
    )
    help_keys_label.pack()

def mol_kalkulator():
    clear_content()
    mol_kalkulator_v3.tkinter_del(content_frame)

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
    row = 0, 
    sticky= "ns"
)


meny_frame.grid()
meny_mellomrom_label = ttk.Label(
    meny_frame,
    text = ""
)

#About_me knapp
meny_mellomrom_label.pack()
meny_about_me_button = ttk.Button(
    meny_frame, 
    text = "About Me (Hobbies etc)", 
    command= about_me, 
    width= 33
)
meny_about_me_button.pack(
    ipady = 20
)
proff_knapp = ttk.Button(
    meny_frame, 
    text = "Information", 
    command= proff, 
    width= 33
)
proff_knapp.pack(
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
    sticky= "nw"
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
    sticky= "nwes"
)

#-----------------------------------------------------
#Keys
#-----------------------------------------------------
def keys(event):
    global lås
    key = event.keysym
    if key.lower() == "m":
        meny()
    elif key == "Escape":
        window.destroy()
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