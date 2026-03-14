
#Oppgave 1 - Rektangel
class Rektangel:
    def __init__(self, bredde, høyde):
        self.bredde = bredde
        self.høyde = høyde

    def areal(self):
        return self.bredde * self.høyde
    
    def omkrets(self):
        return 2*(self.bredde + self.høyde)
    
a = Rektangel(10, 5)

print(a.areal())
print(a.omkrets())

#Oppgave 2 - Bok
class bok:
    def __init__(self, tittel, forfatter, sider):
        self.tittel = tittel
        self.forfatter = forfatter
        self.sider = sider

    def lesetid(self):
        lesetid = self.sider / 50
        return lesetid
    
    def __str__(self):
        return(f"{self.tittel} er skrevet av {self.forfatter} og har {self.sider} sider.")

b = bok("Harry_Potter", "J.K_Rowling", 356)

print(b.lesetid())
print(b)

#Oppgave 3 - Vare
class Vare:
    def __init__(self, navn, pris):
        self.navn = navn
        self.pris = pris

    def sett_pris(self, ny_pris):
        if ny_pris > 0:
            self.pris = ny_pris
            True
        else: 
            print("Ugyldig pris, prisen må være større enn 0")

    def hent_info(self):
        return (f"Vare: {self.navn}, Pris: {self.pris:.2f} kr")
    
melk = Vare("Lettmelk", 25.50)



