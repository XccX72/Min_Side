class Ansatt:
    def __init__(self, fornavn: str, etternavn: str, epost: str, ansatt_id: int):
        self.ansatt_id = ansatt_id
        self.fornavn = fornavn
        self.etternavn = etternavn
        self.epost = epost

    ansatt_register = []

    def registrer_ansatt(self):
        Ansatt.ansatt_register.append(self)

    def fjern_ansatt(self):
        Ansatt.ansatt_register.remove(self)

    def skriv_ansatt_liste(self):
        return Ansatt.ansatt_register

    def fullt_navn(self):
        return (f"{self.fornavn} {self.etternavn}")
    
    def beregn_lønn(self):
        return 0

    def vis_profil(self):
        return (f"Fullt Navn: {self.fullt_navn()}. ID: {self.ansatt_id}. Epost: {self.epost}")
    
class FastAnsatt(Ansatt):
    def __init__(self, fornavn: str, etternavn: str, årslønn: float, ansatt_id: int, epost: str):
        super().__init__(fornavn, etternavn, epost, ansatt_id)
        self.årslønn = årslønn

    def beregn_lønn(self):
        return (f"Årslønn: {self.årslønn / 12}")
    
class TimeAnsatt(Ansatt):
    def __init__(self, fornavn: str, etternavn: str, epost: str, ansatt_id: int, timesats: int, timer_arbeid: int):
        super().__init__(fornavn, etternavn, epost, ansatt_id)
        self.timesats = timesats
        self.timerarbeid = timer_arbeid

    def beregn_lønn(self):
        return (f"Lønn: {self.timesats * self.timerarbeid}")
    
    def registrer_timer(self, antalltimer):
        self.timerarbeid += antalltimer
        return self.timerarbeid
    
class ProvisjonsSelger(Ansatt):
    def __init__(self, fornavn: str, etternavn: str, epost: str, ansatt_id: int, grunnlønn: float, provisjonsfaktor: float, salgsum_denne_mnd: float):
        super().__init__(fornavn, etternavn, epost, ansatt_id)
        self.provisjonsfaktor = provisjonsfaktor
        self.salgsum_denne_mnd = salgsum_denne_mnd
        self.grunnlønn = grunnlønn

    def beregn_lønn(self):
        a = self.grunnlønn + (self.salgsum_denne_mnd*self.provisjonsfaktor)
        return (a)
    
    def registrer_salg(self, beløp):
        self.salgsum_denne_mnd += beløp
        return self.salgsum_denne_mnd
    
class Bob:
    def __init__(self, navn):
        self.navn = navn


p1 = FastAnsatt("Emil", "Thune", 530000, 12345, "e-emil@gmail.com")
p2 = TimeAnsatt("Aline", "Spriet", "aline.spriet@gmail.com", 3214, 150, 5)
p3 = ProvisjonsSelger("Magnus", "Kaastad", "e-magnus@gmail.com", 9867, 3000, 50, 2460)
p4 = Ansatt("Danni", "Spriet", "e-danspr@gmail.com", 7654)
p5 = Bob("Erik")

p1.registrer_ansatt()
p2.registrer_ansatt()
p3.registrer_ansatt()
p4.registrer_ansatt()

p1.beregn_lønn()
p2.beregn_lønn()
p3.beregn_lønn()

p2.registrer_timer(5)
p2.beregn_lønn()

p3.registrer_salg(500)
p3.beregn_lønn()

print(p4.skriv_ansatt_liste())

for x in Ansatt.ansatt_register:
    print(x.vis_profil())
    print(x.beregn_lønn())

def sjekking(objekt):
    if isinstance(objekt, Ansatt):
        if isinstance(objekt, FastAnsatt):
            return(f"Type: Fast Ansatt")
        elif isinstance(objekt, ProvisjonsSelger):
            return (f"Type: Provisjons Selger")
        elif isinstance(objekt, TimeAnsatt):
            return (f"Type: Time Ansatt")
        else:
            return (f"Type: Ansatt")
    else:
        return (f"Type: Ikke Ansatt")
    
print(sjekking(p1))
print(sjekking(p2))
print(sjekking(p3))
print(sjekking(p4))
print(sjekking(p5))






