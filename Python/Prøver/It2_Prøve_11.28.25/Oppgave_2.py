class Person:
    def __init__(self, fornavn, etternavn, fodselsaar):
        self.fornavn = fornavn
        self.etternavn = etternavn
        self.fodselsaar = fodselsaar

    def fullt_navn(self):
        return (f"Ditt fulle navn er {self.fornavn} {self.etternavn} og du ble født i {self.fodselsaar}")
    
class Elev(Person):
    def __init__(self, fornavn, etternavn, fodselsaar, klasse, programområde):
        super().__init__(fornavn, etternavn, fodselsaar)
        self.klasse = klasse
        self.programområde = programområde

    def presentasjon(self):
        return (f"Navn: {self.fornavn}, {self.etternavn}. Klasse: {self.klasse}. Programområde: {self.programområde}")

class Ansatt(Person):
    def __init__(self, fornavn, etternavn, fodselsaar, stilling, avdeling):
        super().__init__(fornavn, etternavn, fodselsaar)
        self.stilling = stilling
        self.avdeling = avdeling
#Glemte å skrive {self.fornavn}
    def signatur(self):
        return (f"Mvh. {self.navn}, {self.stilling}, {self.avdeling}")
    
p1 = Elev("Danni", "Spriet", 2008, "2stb", "Realfag")
p2 = Elev("Fredrikke", "Bahus", 2008, "2sta", "Realfag")
p3 = Elev("Erlend", "Pedersen", 2008, "2sta", "SSØ")

p4 = Person("ALine", "Sarht", 2001)
p5 = Person("Mads", "Oldervik", 2004)

p6 = Ansatt("Emil", "Thune", 1992, "Lærer", "Realfag")
p7 = Ansatt("Anja", "Vet ikke etternavnet hennes", 1984, "Lærer", "Realfag")

p4.fullt_navn()
p1.fullt_navn()
p2.fullt_navn()
p3.fullt_navn()
p5.fullt_navn()
p6.fullt_navn()
p7.fullt_navn()

p1.presentasjon()
p2.presentasjon()
p3.presentasjon()

p6.signatur()
p7.signatur()
