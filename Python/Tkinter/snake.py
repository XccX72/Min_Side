import tkinter as tk
import random
from PIL import Image, ImageTk

class SnakeGame:
    def __init__(self, DELAY_MS = 120):
        # -----------------------------
        # 1) Grunninnstillinger
        # -----------------------------
        self.root = tk.Tk()
        self.root.title("Snake (Canvas + Tkinter)")

        # Rutenett-størrelse (antall celler bortover og nedover)
        self.GRID_W = 20
        self.GRID_H = 20

        # Pikselstørrelse per celle (hvor stor hver rute tegnes)
        self.CELL = 25

        img = Image.open("Tkinter/tomato.png")
        img = img.resize((self.CELL, self.CELL))
        self.food_image = ImageTk.PhotoImage(img)

        # Vindusstørrelse i piksler (canvas)
        self.W = self.GRID_W * self.CELL
        self.H = self.GRID_H * self.CELL

        # Hastighet: lavere = raskere (millisekund per steg)
        self.DELAY_MS = DELAY_MS

        # -----------------------------
        # 2) Canvas (tegneflate)
        # -----------------------------
        self.canvas = tk.Canvas(self.root, width=self.W, height=self.H, bg="white")
        self.canvas.pack()

        # -----------------------------
        # 3) Spillets datastrukturer
        # -----------------------------
        # Slangen representeres som en liste med (x, y)-celler.
        # Første element er hodet.
        self.snake = [(10, 10), (9, 10), (8, 10)]

        # Retning er et (dx, dy) i rutenett-koordinater
        self.direction = (1, 0)  # starter mot høyre

        # For å unngå at man kan snu 180 grader direkte:
        self.next_direction = self.direction

        # Matposisjon (x, y)
        self.food = None
        self.gull_eple = None
        self.place_food()
        self.place_gull_eple()

        self.score = 0
        self.game_over = False

        # -----------------------------
        # 4) Input (piltaster)
        # -----------------------------
        # bind_all gjør at vinduet fanger tastetrykk selv om canvas har fokus
        self.root.bind_all("<KeyPress>", self.on_key)

        # Tegn starttilstand og start game-loop
        self.draw()
        self.loop()

        self.root.mainloop()

    # ------------------------------------------------------------
    # Input
    # ------------------------------------------------------------
    def on_key(self, event):
        """Oppdater ønsket retning basert på piltaster."""
        key = event.keysym

        # Mapping fra tast til (dx, dy)
        if key.lower() == "w" or key == "Up":
            new_dir = (0, -1)
        elif key.lower() == "s" or key == "Down":
            new_dir = (0, 1)
        elif key.lower() == "a" or key == "Left":
            new_dir = (-1, 0)
        elif key.lower() == "d" or key == "Right":
            new_dir = (1, 0)
        elif key.lower() == "e":
            self.change_MS_neg()
            return
        elif key.lower() == "q":
            self.change_MS_pos()
            return
            # Restart med R
        elif key.lower() == "r":
            self.reset_game()
            return
        else:
            return  # ignorer andre taster


        # Forby direkte 180-graders vending:
        # Hvis vi går (1,0) kan vi ikke gå (-1,0) med en gang osv.
        dx, dy = self.direction
        ndx, ndy = new_dir
        if (dx + ndx, dy + ndy) == (0, 0):
            return

        self.next_direction = new_dir

    # ------------------------------------------------------------
    # Spill-logikk
    # ------------------------------------------------------------
    def place_food(self):
        """Plasser mat på en tilfeldig celle som ikke er inni slangen."""
        occupied = set(self.snake)
        if self.gull_eple != None:
            occupied = set(self.snake) | set(self.gull_eple)
        while True:
            x = random.randrange(self.GRID_W)
            y = random.randrange(self.GRID_H)
            if (x, y) not in occupied:
                self.food = (x, y)
                return
            
    def place_gull_eple(self):
        if random.randint(1, 10) == 1:
            occupied = set(self.snake)
            if self.food != None:
                occupied = set(self.snake) | set(self.food)
            
            while True:
                x = random.randrange(self.GRID_W)
                y = random.randrange(self.GRID_H)
                if (x,y) not in occupied:
                    self.gull_eple = (x,y)
                    return
        else:
            return

    def step(self):
        """Utfør ett steg i spillet: flytt slangen, sjekk kollisjoner, spising."""
        # Bruk retningen som sist ble valgt (trygt oppdatert)
        self.direction = self.next_direction
        dx, dy = self.direction

        head_x, head_y = self.snake[0]
        new_head = (head_x + dx, head_y + dy)

        # 1) Kollisjon med vegg
        if not (0 <= new_head[0] < self.GRID_W and 0 <= new_head[1] < self.GRID_H):
            self.game_over = True
            return

        # 2) Kollisjon med seg selv
        # Merk: i vanlig snake er det lov å flytte inn i den siste halen
        # hvis halen samtidig flyttes vekk. For enkelhet sjekker vi hele kroppen.
        if new_head in self.snake:
            self.game_over = True
            return

        # 3) Flytt: legg nytt hode først
        self.snake.insert(0, new_head)

        # 4) Spiser mat?
        if new_head == self.food:
            self.score += 1
            self.place_food()
            self.place_gull_eple()
            # Når vi spiser: ikke fjern halen -> slangen vokser
        elif new_head == self.gull_eple:
            self.score += 5
            self.gull_eple = None
        else:
            # Når vi ikke spiser: fjern siste ledd (halen) for å beholde lengde
            self.snake.pop()

    # ------------------------------------------------------------
    # Tegning på Canvas
    # ------------------------------------------------------------
    def drav_bord(self):
        """Tegner rutene for bretter"""
        for k in range(self.GRID_W):
            for r in range(self.GRID_H):
                x1 = r* self.CELL
                y1 = k*self.CELL
                x2 = x1 + self.CELL
                y2 = y1 + self.CELL

                """Gjør at annenhver rute er forskjellige farger feks Sjakkbrett"""
                if (r+k) % 2 == 0:
                    farge = "#3cbb1c"
                else:
                    farge = "#48e753"
                self.canvas.create_rectangle(x1, y1, x2, y2, fill = farge, outline = "")

    def draw_cell(self, x, y, fill):
        """Tegn en rute (x,y) i rutenettet so   m et rektangel på canvas."""
        x1 = x * self.CELL
        y1 = y * self.CELL
        x2 = x1 + self.CELL
        y2 = y1 + self.CELL
        self.canvas.create_rectangle(x1, y1, x2, y2, fill=fill, outline="black")

    def draw(self):
        """Tegn hele brettet (enkel redraw for læring)."""
        self.canvas.delete("all")

        # (Valgfritt) tegn et svakt "grid" ved å tegne bakgrunnsceller
        # For enkelhet: vi dropper det her og tegner bare slang/mat.

        #Tegne selve brettet
        self.drav_bord()

        # Tegn mat
        fx, fy = self.food
        self.canvas.create_image(
            fx*self.CELL, 
            fy*self.CELL, 
            anchor = "nw", 
            image=self.food_image)
        
        if self.gull_eple != None and len(self.gull_eple) > 0:
            ox, oy = self.gull_eple
            self.draw_cell(ox, oy, fill= "gold")

        # Tegn slange (hode litt mørkere)
        for i, (x, y) in enumerate(self.snake):
            if i == 0:
                self.draw_cell(x, y, fill="royalblue")  # hode
            else:
                self.draw_cell(x, y, fill="skyblue")  # kropp

        # Tekst med score
        self.canvas.create_text(
            10, 10, anchor="nw",
            text=f"Score: {self.score}",
            font=("Arial", 14, "bold")
        )
        #Tekst for fart
        self.canvas.create_text(
            self.W - 10, 5, anchor= "ne", 
            text = f"Speed = {self.DELAY_MS}",
            font = ("Arial", 14)
        )

        # Game over-tekst
        if self.game_over:
            self.canvas.create_text(
                self.W / 2, self.H / 2,
                text="GAME OVER",
                font=("Arial", 28, "bold")
            )
            self.canvas.create_text(
                self.W / 2, self.H / 2 + 40,
                text="R = Restart   Esc = Avslutt",
                font=("Arial", 14)
            )
            self.canvas.create_text(
                self.W / 2, self.H / 2 + 80, 
                text = "Q = Slower Speed   E = Faster Speed", 
                font = ("Arial", 14)
            )
           
    # ------------------------------------------------------------
    # Reset game
    # ------------------------------------------------------------ 
    def reset_game(self):
        """Starter spillet på nytt."""
        self.snake = [(10, 10), (9, 10), (8, 10)]
        self.direction = (1, 0)
        self.next_direction = self.direction

        self.score = 0
        self.game_over = False

        self.place_food()
        self.DELAY_MS

#-----------------------------------------------------------------
#Speed
#-----------------------------------------------------------------
    def change_MS_pos(self):
        if self.DELAY_MS < 210:
            self.DELAY_MS += 30
        else:
            self.DELAY_MS
        return

    def change_MS_neg(self):
        if self.DELAY_MS > 30:
            self.DELAY_MS -= 30
        else:
            self.DELAY_MS
        return
    # ------------------------------------------------------------
    # Game loop
    # ------------------------------------------------------------
    def loop(self):
        """
        Kalles igjen og igjen via after().
        Dette er den vanlige måten å lage animasjon/spill i tkinter.
        """
        # Ekstra: Esc avslutter
        if self.root.focus_displayof():
            self.root.bind_all("<Escape>", lambda e: self.root.destroy())

        if not self.game_over:
            self.step()

        self.draw()
        self.root.after(self.DELAY_MS, self.loop)


if __name__ == "__main__":
    SnakeGame()

