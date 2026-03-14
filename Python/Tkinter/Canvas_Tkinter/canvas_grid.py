import tkinter as tk

# Innstillinger for griden
RUTE_STR = 50  # Størrelse på hver rute i piksler
RADER = 9
KOLONNER = 9


def klikk_håndtering(event):
    # Finn ID-en til objektet som er akkurat der musa peker
    # find_closest returnerer en liste, så vi henter ut det første elementet [0]
    items = canvas.find_closest(event.x, event.y)

    if items:
        item_id = items[0]
        
        # Henter nåværende farge
        gjeldende_farge = canvas.itemcget(item_id, "fill")
        
        # Bytter farge mellom hvit og oransje
        ny_farge = "orange" if gjeldende_farge == "white" else "white"
        canvas.itemconfig(item_id, fill=ny_farge)

window = tk.Tk()
window.title("Canvas Grid 3x3")

# Lag canvas som passer akkurat til 3x3 ruter
canvas = tk.Canvas(window, width=KOLONNER*RUTE_STR, height=RADER*RUTE_STR, bg="white")
canvas.pack(padx=10, pady=10)

# Tegn griden med dobbel for-løkke
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