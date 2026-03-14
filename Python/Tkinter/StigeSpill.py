import tkinter as tk
import random as rnd

window = tk.Tk()
#Gjør at den åpner over hele vinduet
window.state("zoomed")
window.title("Stigespill")

#----------------------------------------
#Basic Info
#----------------------------------------
RUTE_STØRRELSE = 75
KOLONNER = 8
RADER = 8
spiller_posisjon = 0
spiller_figure = None
dice_label = None


Brett_Canvas = tk.Canvas(
    window, 
    width = KOLONNER*RUTE_STØRRELSE, 
    height = RADER*RUTE_STØRRELSE
)
Brett_Canvas.place(
    #Relx/Rely er hvor den plasseres
    #0.5 er midt på skjermen, 1 er helt til høyre
    relx = 0.5, 
    rely = 0.5, 
    anchor= "center"
)

#----------------------------------------------
# Tegner brett
#-----------------------------------------------
def draw_bord():
    count = 1
    for k in range(KOLONNER):
        for r in range(RADER):
            x1 = k * RUTE_STØRRELSE
            y1 = r * RUTE_STØRRELSE
            x2 = x1 + RUTE_STØRRELSE
            y2 = y1 + RUTE_STØRRELSE
            count +=1

            count_liste_rød = [3, 8, 20, 32, 45]
            count_liste_grønn = [12, 25, 37, 50, 62]
            count_start_rute = [9]
            count_slutt_rute = [2]


            if count in count_liste_rød:
                farge = "red"
            elif count in count_liste_grønn:
                farge = "green"
            elif count in count_slutt_rute:
                farge = "blue"
            elif count in count_start_rute:
                farge = "pink"
            else:
                if (r+k) % 2 == 0:
                    farge = "white"
                else:
                    farge = "orange"
            Brett_Canvas.create_rectangle(x1, y1, x2, y2, fill = farge, outline= "")
draw_bord()

#---------------------------------------
#Knapper
#--------------------------------------
def keys(event):
    key = event.keysym

    if key.lower() == "m":
        meny()
    elif key == "Escape":
        window.destroy()
    elif key.lower() == "r":
        dice_kast()
    else:
        return
window.bind_all("<KeyPress>", keys)

#--------------------------------------------
# Dice & Info
#--------------------------------------------

def dice_kast():
    global spiller_posisjon, spiller_figure
    kast_verdi = rnd.randint(1, 6)
    # Her må vi sjekke om dice_label eksisterer før vi oppdaterer den
    # (Siden dice_frame kanskje ikke er laget ennå)
    
    if dice_label is not None:
        dice_label.configure(text = kast_verdi)

    if spiller_posisjon == 0:
        spiller_posisjon = 1

    spiller_posisjon += kast_verdi

    if spiller_posisjon >= 64: 
        spiller_posisjon = 64
        nye_coords = finn_koordinater(spiller_posisjon)
        Brett_Canvas.coords(spiller_figure, *nye_coords)
        game_over()
        return

    nye_coords = finn_koordinater(spiller_posisjon)
    Brett_Canvas.coords(spiller_figure, *nye_coords)

def dice():
    global dice_label
        
    dice_frame = tk.Frame(
        window, 
        bg = "#F57C00", 
        highlightbackground= "black", 
        highlightthickness= 2, 
        padx= 2, 
        pady = 2
    )
    dice_frame.place(
        relx = 0.15, 
        rely = 0.15, 
        anchor= "center"
    )
    dice_label_text = tk.Label(
        dice_frame, 
        text = "Terninkast \n verdi: ", 
        bg = "#F57C00", 
        font = ("Arial", 20)
    )
    dice_label_text.pack()
    dice_label = tk.Label(
        dice_frame, 
        text = "Terninkast", 
        bg = "#F57C00", 
        font= ("Arial", 20)
    )
    dice_label.pack()
    dice_button = tk.Button(
        dice_frame, 
        command = dice_kast, 
        bg = "#F57C00", 
        padx = 20
    )
    dice_button.pack()

dice()

def info_label():
    label_info = tk.Label(
        window, 
        text = "Keys:\nM = Meny\nR = Roll Dice", 
        bg = "#F57C00",     
        font = ("Arial", 20), 
        highlightbackground= "black", 
        highlightthickness= 2
    )
    label_info.place(
        relx = 0.15, 
        rely = 0.40, 
        anchor= "center"
    )

info_label()

#----------------------------------------------
# Meny
#----------------------------------------------
meny_lås = False
def meny():
    global meny_lås

    if meny_lås:
        return
    
    meny_lås = True

    def lukk_meny():
        global meny_lås
        meny_frame.destroy()
        meny_lås = False

    meny_frame = tk.Frame(
        window, 
        bg = "#F57C00", 
        highlightbackground= "black", 
        highlightthickness= 2,
        padx = 20, 
        pady = 20
    )
    meny_frame.place(
        relx = 0.5, 
        rely = 0.5, 
        anchor= "center"
    )

    meny_label = tk.Label(
        meny_frame, 
        text = "Meny", 
        bg = "#F57C00", 
        font = ("Arial", 20)
    )
    meny_label.pack()

    meny_reset = tk.Button(
        meny_frame, 
        text = "Reset Game",
        bg = "#F57C00", 
        command = reset_game
    )
    meny_reset.pack()

    meny_key_button = tk.Button(
        meny_frame, 
        text = "Keys", 
        bg = "#F57C00", 
        command = meny_key
    )
    meny_key_button.pack()

    meny_destroy = tk.Button(
        meny_frame, 
        text ="Lukk", 
        bg= "#F57C00", 
        command = lukk_meny
    )
    meny_destroy.pack()

    meny_game_destroy = tk.Button(
        meny_frame, 
        text = "Lukk Spill", 
        bg = "#F57C00", 
        command = destroy_spill
    )
    meny_game_destroy.pack()

def meny_game_over():
    meny_frame = tk.Frame(
        window, 
        bg = "#F57C00", 
        highlightbackground= "black", 
        highlightthickness= 2,
        padx = 20, 
        pady = 20
    )
    meny_frame.place(
        relx = 0.5, 
        rely = 0.5, 
        anchor= "center"
    )

    meny_label = tk.Label(
        meny_frame, 
        text = "Meny", 
        bg = "#F57C00", 
        font = ("Arial", 20)
    )
    meny_label.pack()

    meny_reset = tk.Button(
        meny_frame, 
        text = "Reset Game",
        bg = "#F57C00", 
        command = reset_game
    )
    meny_reset.pack()

    meny_key_button = tk.Button(
        meny_frame, 
        text = "Keys", 
        bg = "#F57C00", 
        command = meny_key
    )
    meny_key_button.pack()

    meny_game_destroy = tk.Button(
        meny_frame, 
        text = "Lukk Spill", 
        bg = "#F57C00", 
        command = destroy_spill
    )
    meny_game_destroy.pack()

meny_key_lås = False

def meny_key():
    global meny_key_lås

    if meny_key_lås:
        return
    
    meny_key_lås = True
    def key_lukk():
        global meny_key_lås
        key_frame.destroy()
        meny_key_lås = False

    key_frame = tk.Frame(
        window, 
        bg = "#F57C00", 
        highlightbackground= "black", 
        highlightthickness= 2,
        padx = 20, 
        pady = 20
    )
    key_frame.place(
        relx = 0.5, 
        rely = 0.5, 
        anchor= "center"
    )
    key_label = tk.Label(
        key_frame, 
        text = "m = Meny\nr = Roll Dice\nEsc = End Game", 
        bg = "#F57C00"
    )
    key_label.pack()

    key_lukk_button = tk.Button(
        key_frame, 
        bg = "#F57C00", 
        text = "Lukk", 
        command = key_lukk
    )
    key_lukk_button.pack()

#------------------------------------------------
# Spiller
#------------------------------------------------
def spiller():
    global spiller_figure
    coords = finn_koordinater(1)
    coords_1 = finn_koordinater(1)


    spiller1 = Brett_Canvas.create_rectangle(coords, fill = "black", outline= "white")

    spiller2 = Brett_Canvas.create_rectangle(coords_1, fill = "gray", outline = "black")

    return spiller1

def finn_koordinater(posisjon):
    # Juster posisjon så den starter på 0 for matte-logikk (0-63)
    p = posisjon - 1 
    
    rad = p // KOLONNER
    kol = p % KOLONNER

    # Logikk for stigespill (siksak-mønster)
    # Annethvert lag går fra høyre til venstre
    if rad % 2 == 1:
        kol = (KOLONNER - 1) - kol

    # Snu raden så rute 1 er nederst
    visuell_rad = (RADER - 1) - rad

    x1 = kol * RUTE_STØRRELSE + 15
    y1 = visuell_rad * RUTE_STØRRELSE + 15
    x2 = (kol + 1) * RUTE_STØRRELSE - 15
    y2 = (visuell_rad + 1) * RUTE_STØRRELSE - 15
    
    return x1, y1, x2, y2

#------------------------------------------------
#Destroy / Reset 
#------------------------------------------------
def reset_game():
    start_spill()

#Hvis du vinner spillet (skal restarte og boote opp meny)
def game_over():
    game_over_frame = tk.Frame(
        window, 
        bg = "#F57C00", 
        highlightbackground= "black", 
        highlightthickness= 2,
        padx = 20, 
        pady = 20
    )
    game_over_frame.place(
        relx = 0.5, 
        rely = 0.2, 
        anchor= "center"
    )
    game_over_label = tk.Label(
        game_over_frame, 
        text = "You win!", 
        bg = "#F57C00", 
        font = ("Arial", 30)
    )
    game_over_label.pack()
    meny_game_over()


def destroy_spill():
    window.destroy()

def start_spill():
    pass

spiller_figure = spiller()

window.mainloop()