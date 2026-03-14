import tkinter as tk


window = tk.Tk()
window.state("zoomed")
window.title("Chess")

#----------------------------------------
#Lage Brett
#----------------------------------------
RUTE_STØRRELSE = 75
KOLONNER = 8
RADER = 8

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

def draw_bord():
    for k in range(KOLONNER):
        for r in range(RADER):
            x1 = k * RUTE_STØRRELSE
            y1 = r * RUTE_STØRRELSE
            x2 = x1 + RUTE_STØRRELSE
            y2 = y1 + RUTE_STØRRELSE

            if (r+k) % 2 == 0:
                farge = "white"
            else:
                farge = "seagreen4"

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
    else:
        return

window.bind_all("<KeyPress>", keys)



def meny():
    meny_frame = tk.Frame(
        window, 
        bg = "gray", 
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
        bg = "gray", 
        font = ("Arial", 20)
    )
    meny_label.pack()

    meny_reset = tk.Button(
        meny_frame, 
        text = "Reset Game",
        bg = "gray", 
        command = reset_game
    )
    meny_reset.pack()

    meny_destroy = tk.Button(
        meny_frame, 
        text ="Lukk", 
        bg= "gray", 
        command = meny_frame.destroy
    )
    meny_destroy.pack()

def reset_game():
    pass

window.mainloop()


