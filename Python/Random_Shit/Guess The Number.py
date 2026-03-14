import random as rnd

tilfeldigTall = rnd.randint(0, 10000)
antallForsok = 0
gjett = -1

while tilfeldigTall != gjett:
    gjett = int(input("Gjett tall: "))
    if gjett < tilfeldigTall:
        print ("Du gjetter for lavt, prrøv igjen!")
        antallForsok = antallForsok + 1
    elif gjett > tilfeldigTall:
        print ("DU gjetter for høyt, prøv igjen!")
        antallForsok = antallForsok + 1
    
print ("Yay du greide det, du brukte", antallForsok)