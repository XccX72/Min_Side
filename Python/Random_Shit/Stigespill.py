import numpy as np
import random as rnd

print("Velkommen til Stigespill, du vinenr hvis du når 100 poeng")

antSpil = int(input("Hvor mange folk?"))

arr = []

for _ in range(antSpil):
    arr.append(0)

terning = 0

antallGang = 0

def t():
    t1 = rnd.randint(1,6)
    t2 = rnd.randint(1,6)
    terning = t1 + t2
    return terning    

while max(arr) < 100 :
    rød = [rnd.randint(1,100) for h in range (15)]
    grønn = [rnd.randint(1,100) for k in range (15)]

    for p in range(antSpil):
        a = rnd.randint(1,50)

        inputPlayer = str(input("Skriv trill for å trille terning - " )).lower()

        if inputPlayer == "trill":

            arr[p] = arr[p] + t()

            antallGang = antallGang +1

            if arr[p] == rød:
                arr[p] = arr[p] - a

            elif arr[p] == grønn:
                arr[p] = arr[p] + a

            else:
                arr[p] = arr[p]

            if arr[p] > 100: print (f"Du brukte {antallGang} for å vinne, og du fikk {arr[p]}")

            print(f"{p+1} : antallgang : {antallGang} Poeng : {arr[p]}")

        elif inputPlayer == "end":
            break
        else:
            print("Du spiller ikke spillet")