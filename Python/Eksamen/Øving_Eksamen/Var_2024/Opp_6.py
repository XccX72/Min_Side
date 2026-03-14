class Calc:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def pluss(self):
        try:
            return self.a + self.b
        except:
            return ("Det gikk ikke ")
    
    def minus(self):
        try:
            return self.a - self.b
        except:
            return ("Det gikk ikke ")
    
    def ganging(self):
        try:
            return self.a * self.b
        except:
            return ("Det gikk ikke ")

    def dele(self):
        try:
            return self.a / self.b
        except:
            return ("Det gikk ikke ")
        

a1 = Calc(5, 2)

print(a1.dele())
print(a1.pluss())
print(a1.minus())
print(a1.ganging())
    