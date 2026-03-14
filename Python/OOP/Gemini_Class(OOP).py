class Bil:
    def __init__(self, merke, modell, kmstand):
        self.merke = merke
        self.modell = modell
        self.kmstand = kmstand

    def vis_info(self):
        print(self.merke, self.modell, "-", self.kmstand)


bil1 = Bil("Toyata", "Corella", 64000)
bil1.vis_info()


class Elev:
    def __init__(self, navn, alder):
        self.navn = navn
        self.alder = alder
        self.karakter = []

    def karakterListe(self, karakter):
        self.karakter.append(karakter)
    
    def snittKarakter(self):
        if len(self.karakter) == 0:
            return 0.0

        c = sum(self.karakter) / len(self.karakter)
        return c
    
    def antllFag(self):
        d = len(self.karakter)
        return d       
    
    def info(self):
        e = self.snittKarakter()
        return (f"Eleven heter {self.navn}, alder:{self.alder} og har snittkarakter {e}")

class Ansatt:
    def __init__(self, navn, lønn):
        self.navn = navn
        self.lønn = lønn

    def vis_info(self):
        return (f"Ansatt Info \nNavn: {self.navn} \nLønn: {self.lønn}")

class Lærer(Ansatt):
    def __init__(self, fag, navn, lønn):
        self.fag = fag
        super().__init__(navn, lønn)

    def vis_info(self):
        return (f"Ansatt Info \nNavn: {self.navn} \nLønn: {self.lønn} \nFag: {self.fag}")
    
class Rektor(Lærer):
    def __init__(self, antall, navn, lønn, fag):
        self.antall = antall
        super().__init__(navn, lønn, fag)

    def lønnkostnad(self, ansattliste):
        lønn = [objekt.lønn for objekt in ansattliste]

        totalKostnad = sum(lønn)

        return totalKostnad
            
class Temperaturmåling:
    def __init__(self):
        self.__målinger = []
        
    def legg_til_måling(self, temp):
        return self.__målinger.append(temp)
    
    def hent_antall_måling(self):
        return len(self.__målinger)

    @property
    def gjennomsnit(self):
        if len(self.__målinger) <= 0: 
            return None
        return sum(self.__målinger) / len(self.__målinger)

def sum_partall(limit):
        x = 1
        y = 0
        while x < limit:
            if x % 2 == 0:
                 y += x
            x += 1
        return (y)

def fizz_buzz(n):
    for x in range(1, n + 1):
        if x % 3 == 0 and x % 5 == 0:
            print("Fizzbuzz")
        elif x % 3 == 0:
            print("Fizz")
        elif x % 5 == 0:
            print("Buzz")
        elif x % 3 != 0 or x % 5 != 0:
            print(x)

