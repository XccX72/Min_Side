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

    def signatur(self):
        return (f"Mvh. {self.navn}, {self.stilling}, {self.avdeling}")
    
p1 = Elev("Danni", "Spriet", 2008, "2stb", "Realfag")
p2 = Elev("Fredrikke", "Bahus", 2008, "2sta", "Realfag")
p3 = Elev("Erlend", "Pedersen", 2008, "2sta", "SSØ")

p4 = Person("ALine", "Sarht", 2001)
p5 = Person("Mads", "Oldervik", 2004)

p6 = Ansatt("Emil", "Thune", 1992, "Lærer", "Realfag")
p7 = Ansatt("Anja", "Vet ikke etternavnet hennes", 1984, "Lærer", "Realfag")

class Arrangement:
    def __init__(self, navn, dato, maks_plasser, ansvarlig):
        self.navn = navn
        self.dato = dato
        self.maks_plasser = maks_plasser
        self.ansvarlig = ansvarlig
        self.deltakere = []

    def registrer_deltaker(self, x):
        if len(self.deltakere) == self.maks_plasser:
            return ("Det er ikke mulig, siden det er fullt")
        else:
            self.deltakere.append(x)

    def fjern_deltaker(self, x):
        self.deltakere.remove(x)

    def er_fullt(self): 
        if len(self.deltakere) == self.maks_plasser:
            return ("Det er fullt")
        else:
            return ("Det er ikke fullt")

    def antall_ledige_plasser(self):
        if len(self.deltakere) == self.maks_plasser:
            return ("ingen plasser")
        else:
            return ("Det er ", self.maks_plasser - len(self.deltakere), "plasser igjen")

    def skriv_deltakerliste(self):
        for x in self.deltakere:
            print (x.fornavn)

s1 = Arrangement("Ball", 22.10, 5, "Bahus")

        
p1 = Elev("Danni", "Spriet", 2008, "2stb", "Realfag")
p2 = Elev("Fredrikke", "Bahus", 2008, "2sta", "Realfag")
p3 = Elev("Erlend", "Pedersen", 2008, "2sta", "SSØ")

p4 = Person("ALine", "Sarht", 2001)
p5 = Person("Mads", "Oldervik", 2004)

p6 = Ansatt("Emil", "Thune", 1992, "Lærer", "Realfag")
p7 = Ansatt("Anja", "Vet ikke etternavnet hennes", 1984, "Lærer", "Realfag")

print(s1.registrer_deltaker(p1))
print(s1.registrer_deltaker(p2))
print(s1.registrer_deltaker(p3))
print(s1.registrer_deltaker(p4))
print(s1.registrer_deltaker(p5))
print(s1.registrer_deltaker(p6))
print(s1.fjern_deltaker(p2))
print(s1.fjern_deltaker(p5))
print(s1.skriv_deltakerliste())
print(s1.antall_ledige_plasser())
print(s1.er_fullt())