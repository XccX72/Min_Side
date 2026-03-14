import tkinter as tk
import math

# 1. Oppsett av vinduet
root = tk.Tk()
root.title("Baller uten klasser")

canvas = tk.Canvas(root, width=600, height=400, bg="lightgreen")
canvas.grid(
    column= 0, 
    row = 1, 
)

# 2. Definerer variabler for Ball 1 (Rød)
r1 = 20
x1, y1 = 100, 100
dx1, dy1 = 3, 4
ball1 = canvas.create_oval(x1-r1, y1-r1, x1+r1, y1+r1, fill="red")

# 3. Definerer variabler for Ball 2 (Blå)
r2 = 20
x2, y2 = 500, 300
dx2, dy2 = -4, -3
ball2 = canvas.create_oval(x2-r2, y2-r2, x2+r2, y2+r2, fill="blue")

def flytt_baller():
    global dx1, dy1, dx2, dy2
    
    # Flytt ballene på canvas
    canvas.move(ball1, dx1, dy1)
    canvas.move(ball2, dx2, dy2)
    
    # Hent nye posisjoner [x_start, y_start, x_slutt, y_slutt]
    pos1 = canvas.coords(ball1)
    pos2 = canvas.coords(ball2)
    
    # --- Veggkollisjon Ball 1 ---
    if pos1[0] <= 0 or pos1[2] >= 600: 
        dx1 *= -1
    if pos1[1] <= 0 or pos1[3] >= 400: 
        dy1 *= -1
    
    # --- Veggkollisjon Ball 2 ---
    if pos2[0] <= 0 or pos2[2] >= 600: 
        dx2 *= -1
    if pos2[1] <= 0 or pos2[3] >= 400: 
        dy2 *= -1
    
    # --- Kollisjon mellom ballene ---
    # Finn sentrum av ballene
    sentrum1_x = (pos1[0] + pos1[2]) / 2
    sentrum1_y = (pos1[1] + pos1[3]) / 2
    sentrum2_x = (pos2[0] + pos2[2]) / 2
    sentrum2_y = (pos2[1] + pos2[3]) / 2
    
    # Beregn avstand (Pythagoras)
    avstand = math.sqrt((sentrum2_x - sentrum1_x)**2 + (sentrum2_y - sentrum1_y)**2)
    
    if avstand <= (r1 + r2):
        # Bytt fart (enkel sprette-effekt)
        dx1, dx2 = dx2, dx1
        dy1, dy2 = dy2, dy1
    
    # Kjører neste bilde i animasjonen om 10ms
    root.after(10, flytt_baller)

# Start animasjonen
flytt_baller()

root.mainloop()