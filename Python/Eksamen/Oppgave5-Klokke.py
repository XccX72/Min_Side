class Tallviser:
    def __init__(self, verdi:int, maks_verdi:int):
        self.verdi = verdi
        self.maks_verdi = maks_verdi
    
    def set_verdi(self, int):
        if int < 60 and  int > -1:
            self.verdi = int
            return self.verdi
        
        else:
            return (f"Det går ikke å ha mer enn {self.maks_verdi}")

    def øk(self):
        #Det som øker tiden hvert min
        self.verdi += 1
        return self.verdi

    def vis_verdi(self):
        return self.verdi


min_viser = Tallviser(0, 60)
time_viser = Tallviser(0, 12)

min_viser.vis_verdi()
time_viser.vis_verdi()

class Digitalklokke:
    def __init__(self, Timer:Tallviser, Minutter:Tallviser):
        self.Timer = Timer
        self.Minutter = Minutter

    def set_tid(self, time_int, minutt_int):
        self.Timer.set_verdi(time_int)
        self.Minutter.set_verdi(minutt_int)
        print (f"Klokke -> {self.Timer} - {self.Minutter}")

    def tid_går(self):
        #passer på at nir minuttt = 60 så øker Time ved 1
        if self.Minutter.vis_verdi() >= 60:
            self.Minutter.set_verdi(0)
            self.Timer.øk(1)
        else:
            print ("Det går ikke")

    def vis_tid(self):
        print (f"Klokken er {self.Timer.vis_verdi()} - {self.Minutter.vis_verdi()}")

klokke = Digitalklokke(min_viser, time_viser)

klokke.set_tid(10, 58)
klokke.vis_tid()

