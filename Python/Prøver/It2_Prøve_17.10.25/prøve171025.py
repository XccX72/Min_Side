import math 
import random as rnd

#----Oppgave 1------

def greet(x):
    print(f"Heihei {x} du så veldig pen og smart ut idag")

print(greet("Danni"))

#------Oppgave 2 ------

listeNavn = ["Emil", "Terje", "Allan"]

for i in listeNavn:
    print(f"Hei, {i}")

#------ Oppgave 3 -----

inputAlder = int(input("hva er alderen din"))

if inputAlder < 25:
    print("Du er ung")
elif inputAlder > 65:
    print("Du er gammel")

#----- Oppgave 4 -------

antallGanger = (int(input("hvor mange terninger")))
if antallGanger <= 10:
    if antallGanger >= 1:
        for i in range(antallGanger):
            a =  rnd.randint(1,6)
            print(a)
            b = []
            b.append(a)

        c = sum(b)
        d = sum(b)/antallGanger

        print(f"Gjennomsnittet er {d} og summen på terningene er {c}")
    else:
        print("Må være like 1 eller større")
else:
    print("Kan ikke være mer enn 10")

#----Emil sin versjon av min ----
    b = []

antallGanger = (int(input("hvor mange terninger")))
if antallGanger <= 10 and antallGanger >=1:
    for i in range(antallGanger):
        b.append(rnd.randint(1,6))
        print(b[i])
    c = sum(b)
    d = sum(b)/antallGanger

    print(f"Gjennomsnittet er {d} og summen på terningene er {c}")
else:
    print("Kan ikke være mer enn 10")


#----- Oppgave 5 -------

tekst = input("skriv en tekst")

a = tekst.split()

def analyze(a):
    global tekst
    b = 2*len(a) - 1
    c = tekst

#------- Del 2 ----------





