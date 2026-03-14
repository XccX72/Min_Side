import tkinter as tk

def klikk_håndtering(event):
    # Finn ID-en til objektet som er akkurat der musa peker
    # find_closest returnerer en liste, så vi henter ut det første elementet [0]
    items = canvas.find_closest(event.x, event.y)

    if items:
        item_id = items[0]
        
        # Henter nåværende farge
        gjeldende_farge = canvas.itemcget(item_id, "fill")
        
        # Bytter farge mellom hvit og oransje
        ny_farge = "red" if gjeldende_farge == "white" else "white"
        canvas.itemconfig(item_id, fill=ny_farge)

window = tk.Tk()
window.geometry("350x400")
window.title("Tre På rad")

window.columnconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

KOLONNER = 3
RADER = 3
RUTE_STR = 50

frame_text = tk.Frame(
    window,  
    pady = 10, 
    padx = 30
)
frame_text.grid(
    column= 0, 
    row = 0, 
    sticky= "nswe"
)

frame_canvas = tk.Frame(
    window,
    padx = 100, 
    pady = 100 
)
frame_canvas.grid(
    column=0, 
    row = 1, 
    sticky= "nsew" 
)

text = tk.Label(
    frame_text,
    text = "Tre på Rad", 
    font= ("Arial", 20)
)
text.pack(anchor="center")

canvas = tk.Canvas(
    frame_canvas, 
    width= KOLONNER*RUTE_STR, 
    height= RADER*RUTE_STR, 
    bg = "white",
)
canvas.pack(anchor= "center")

for r in range(RADER):
    for k in range(KOLONNER):
        # Beregn koordinater for hvert rektangel
        x1 = k * RUTE_STR
        y1 = r * RUTE_STR
        x2 = x1 + RUTE_STR
        y2 = y1 + RUTE_STR
        
        # Lag rektanglet og gi det hvit startfarge
        canvas.create_rectangle(x1, y1, x2, y2, fill="white", outline="black")

# Bind venstre museklikk til funksjonen
canvas.bind("<Button-1>", klikk_håndtering)
window.mainloop()