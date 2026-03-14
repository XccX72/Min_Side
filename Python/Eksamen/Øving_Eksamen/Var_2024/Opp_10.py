import tkinter as tk
import random as rnd


class Game:
    def __init__(self):
        #-------------------------------------------------------
        #Basic Shi
        #-------------------------------------------------------
        self.window = tk.Tk()
        self.window.title("Game")
        self.window.state("zoomed")

        self.KOLONNER = 22
        self.RADER = 22
        self.RUTE_STR = 25

        self.W = self.KOLONNER*self.RUTE_STR
        self.H = self.RADER*self.RUTE_STR

        #------------------------------------------------------
        #Canvas (Brettet)
        #------------------------------------------------------
        self.canvas = tk.Canvas(self.window, width=self.W, height=self.H, bg="white")
        self.canvas.pack()

        self.label = tk.Label(self.window, text = "Esc = Close Window\n R = Reset Game")
        self.label.pack()

        #------------------------------------------------------
        #Running av Funksjoner og slutt Tkinter del
        #------------------------------------------------------
        self.start_celle = None
        self.count = 1
        self.count_liste = []

        self.draw_bord(None)
        self.start_celle_func()
        self.slutt_celle_func()


        self.window.bind_all("<KeyPress>", self.keys)
        self.window.mainloop()
    #------------------------------------------------------------
    #Funksjoner
    #------------------------------------------------------------
    #Keys
    def keys(self, event):
        key = event.keysym

        if key == "Escape":
            self.window.destroy()
        elif key.lower() == "r":
            self.reset_game()
        else:
            return
        
    def draw_bord(self, farge):
        a = True

        for k in range(self.KOLONNER):
            for r in range(self.RADER):
                x1 = k * self.RUTE_STR
                y1 = r * self.RUTE_STR
                x2 = x1 + self.RUTE_STR
                y2 = y1 + self.RUTE_STR

                if a == True:
                    farge = "white"
                
                self.canvas.create_rectangle(x1, y1, x2, y2, fill = farge, outline= "black")

    def draw_cell(self, x, y, fill): #Generelt for å plassere "blokker" på canvas
        """Tegn en rute (x,y) i rutenettet so   m et rektangel på canvas."""
        x1 = x * self.RUTE_STR
        y1 = y * self.RUTE_STR
        x2 = x1 + self.RUTE_STR
        y2 = y1 + self.RUTE_STR
        self.canvas.create_rectangle(x1, y1, x2, y2, fill=fill, outline="black")

    def start_celle_func(self):
        sjanse = rnd.randint(1, 3)
        x = rnd.randint(0, 21)
        y = rnd.randint(0, 21)

        if self.start_celle != None:
            return
        else:
            for i in range(1, 484):
                if sjanse == 1:
                    self.draw_cell(x, y, "black")#Bør endre dette til draw_bord()
                    self.count_liste.append((21 * (y-1)) + x)

    def slutt_celle_func(self):
        sjanse = rnd.randint(1, 3)
        while True:
            if self.count in self.count_liste and sjanse == 2:
                farge = "black"
                self.draw_bord(farge)
                self.count += 1

            else:
                return
    
    def reset_game(self):
        self.canvas.destroy()
        self.canvas = tk.Canvas(self.window, width=self.W, height=self.H, bg="white")
        self.canvas.pack()
        self.start_celle = None
        self.draw_bord(None)
        self.start_celle_func()
        self.slutt_celle_func()

if __name__ == "__main__":
    Game()
