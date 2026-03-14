import math as mt

def ganging(x):
    produkt = 1
    for i in x:
        produkt *= i
    return produkt

def deling(x):
    if not x:
        return None
    produkt = x[0]  
    for i in x[1:]:          
        produkt /= i
    return produkt

def pluss(x):
    produkt = 0
    for i in x:
        produkt += i
    return "summen er ", produkt

def minus(x):
    produkt = 0
    for i in x:
        produkt -= i
    return produkt

def potens(x,y):
    return x**y

def root(x,y):
    return x**(1/y)

def meny():
    print("Meny \nTrykk for å gjøre noe")
    print("1 : Pluss \n2 : Minus \n3 : Ganging " \
    "\n4 : Deling \n5 : Potens \n6 : Root \n9 : Meny\n0 : Avslutt ")

    spørring = int(input("Hva skal jeg gjøre? "))

    if spørring == 1:
        b = []
        a = int(input("Hvor mange tall skal adderes - "))
        for _ in range(a):
            c = float(input("Hvilket tall skal jeg addere - "))
            b.append(c)
        print(pluss(b))
        print(meny())

    elif spørring == 2:
        b = []
        a = int(input("Hvor mange tall skal substraktere - "))
        for x in range(a):
            c = float(input("Hvilket tall skal jeg subtrere - "))
            b.append(c)
        print(minus(b))
        print(meny())

    elif spørring == 4:
        b = []
        a = int(input("Hvor mange tall skal deles - "))
        for x in range(a):
            c = float(input("Hvilket tall skal jeg dele - " ))
            if c == 0:
                print("Det er ikke lov!")
                break
            b.append(c)
        print(deling(b))
        print(meny())

    elif spørring == 3: 
        b = []
        a = int(input("Hvor mange tall skal ganges - "))
        for x in range(a):
            c = float(input("Hvilket tall skal jeg ganges - "))
            b.append(c)
        print(ganging(b))
        print(meny())

    elif spørring == 5:
        a = float(input("Hva er grunntallet - "))
        b = float(input("Hva er eksponenten"))
        print(potens(a,b))
        print(meny())

    elif spørring == 6:
        a = float(input("Hva er grunntallet - "))
        b = float(input("Hva er 'root'"))
        print(root(a,b))
        print(meny())

    elif spørring == 0:
        print("Hadet!")
        SystemExit
    
    elif spørring == 9:
        print(meny())

if __name__ == "__main__":
    meny()