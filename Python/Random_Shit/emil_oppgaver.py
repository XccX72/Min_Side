#Øving på Python 9.9.10

import math
import random as rnd
import pandas as pd

# ------ Oppgave 1 ----------

navn = input("Hva er navnet ditt : ")
alder = int(input("Hva er alderen din : "))
favFag = (input("Hva er favorittfaget ditt : "))

print(f"Ditt navn er {navn}, alderen din er {alder} og fav faget ditt er {favFag}")

# --------- Oppgave 2 -----------

tall1 = int(input("tall verdi 1"))
tall2 = int(input("tall verdi 2"))

def f(tall1,tall2):
    z = sum(tall1, tall2)
    return z

def g(tall1,tall2):
    h = tall1-tall2
    return h

def i(tall1,tall2):
    l = tall1 // tall2
    return l

#---------- Oppgave 3 -------------------

matretter = ['Sushi', 'Kebab', 'Pizza', 'Hamburger', 'Pasta']

i = 1
for matretter in matretter:
    print(i, matretter)
    i += 1

#--------Oppgave 4 ------------------

tall = int(input("Gi meg et heltall"))


if tall < 0:
    print("Du har ett negativt tall")

elif tall > 0:
   print("Du har ett positivt tall")

elif tall == 0:
    print("tallet ditt er 0")
    
else:
    print("tallet ditt er ikke et heltall")

 #------- oppgave 5 ------------

 #dfghjklopølkjhgfdsdfghjklkjhg
#dfgtyuiuyrik
#fghjkjhgfddddddddddddddddddddd
#ddddddddddddddddddddddddddd

#------- Tallstatistisk med funksjoner 1 ---------

b = '5 3 3 4 1 7 1 10 9 8 11 6 3 3 4 5 2 6'

ab = [int(s) for s in b.split()]

print(ab)

def minVerdi(ab):
   return (format(min(ab), ".2f"))

print(minVerdi(ab))

def maxVerdi(ab):
    return (max(ab))

print(maxVerdi(ab))

def gjennomsnitt(ab):
    return (sum(ab) / len(ab))
print(gjennomsnitt(ab))

def median(ab):
    c = sorted(ab)
    cl = len(c)

    if cl % 2 == 1:
        return c[cl//2]
    else:
        mid1 = c[cl//2-1]
        mid2 = c[cl//2]
        return (mid1 + mid2) / 2
    
print (median(ab))

mest = max(set(ab), key=ab.count)
print("fghjhfdfgh", mest, "\nfggfgf")

mestt = ab.count

#----- Passord vurdering --------

def a(passord):

    z = len(passord)
    b = any(tegn.isupper() for tegn in passord)
    c = any(tegn1.isupper() for tegn1 in passord)
    d = any(tegn2.isdigit() for tegn2 in passord)
    e = any(not tegn3.isalnum() for tegn3 in passord)

    if z < 8:
        print("Svakt passord \nDu må ha minst 8 tegn i passord!")
        return False
    
    elif b == False:
        print("Svakt passord \nDu har ikke en stor bokstav")
        return False
    
    elif c == False:
        print("Svakt passord \nDu har ikke en liten bokstav")
        return False
    
    elif d == False:
        print("Svakt passord \nDu har ikke en et tall")
        return False
    
    elif e == False:
        print("Svakt passord \nDu har ikke et spesialtegn i passord")
        return False
    
    else:
        print("Sterkt passord")
        return True

while True:
    passord = (input("Et passord"))

    if a(passord):
        break