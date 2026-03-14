import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk

#Oppgave 1

def beregn_areal_rektangel(bredde, lengde):
    return (bredde*lengde)

areal = beregn_areal_rektangel(5, 10)

print(areal)

#Oppgave 2 

def er_partall(tall):
    if tall % 2 == 0:
        return True
    else:
        return False
    
#Oppgave 3

def finn_felles_elementer(liste1, liste2):
    b = []
    for x in liste1:
        if x in liste2:
             b.append(x)
        else:
            continue
    return b        

a = [1, 2, 3, 4, 5]
b = [4, 5, 6, 7, 8]
felles = finn_felles_elementer(a, b)

print(felles)

#Oppgave 4

def tell_vokaler(tekst):
    b = tekst.lower()

    