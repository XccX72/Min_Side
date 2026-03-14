import tkinter as tk

window = tk.Tk()
window.state("zoomed")

#---------------------------------------------------------------------------
#Tegne Brett 
#---------------------------------------------------------------------------
KOLONNER = 22
RADER = 22
RUTE_STR = 25
        
Brett_Canvas = tk.Canvas(
    window, 
    width = KOLONNER*RUTE_STR, 
    height = RADER*RUTE_STR
)
Brett_Canvas.place(
    #Relx/Rely er hvor den plasseres
    #0.5 er midt på skjermen, 1 er helt til høyre
    relx = 0.5, 
    rely = 0.5, 
    anchor= "center"
)
def draw_bord():
    count = 1
    a = True

    for k in range(KOLONNER):
        for r in range(RADER):
            x1 = k * RUTE_STR
            y1 = r * RUTE_STR
            x2 = x1 + RUTE_STR
            y2 = y1 + RUTE_STR
            count +=1

            if a == True:
                farge = "white"
            

            Brett_Canvas.create_rectangle(x1, y1, x2, y2, fill = farge, outline= "black")
draw_bord()



#---------------------------------------------------------------------------------
#Keys
#---------------------------------------------------------------------------------
def keys(event):
    key = event.keysym

    if key == "Escape":
        window.destroy()
    else:
        return
window.bind_all("<KeyPress>", keys)

window.mainloop()
