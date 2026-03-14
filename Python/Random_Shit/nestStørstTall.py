import random as rnd
import numpy as np

#metode 1 -------------------------

a = [5, 3, 6, 3, 8, 10]

a.sort(reverse=True)

for tall in range(len(a)):
    if a[tall] >= a[tall+1]:
        print(a[0])
        break

#metode 2 --------------------

liste = [rnd.randint(-100, 100) for _ in range (25)]

størst = liste[0]
neststørst = liste[1]

if størst > neststørst:
    neststørst = størst
    størst = liste[1]

for i in range(2, len(liste)):
    if liste [i] > størst:
        neststørst = størst
        størst = liste[i]
    
    elif liste[i] > neststørst and liste[i] != størst:
        neststørst = liste[i]

liste.sort(reverse=True)
print(liste)  
print(neststørst)
