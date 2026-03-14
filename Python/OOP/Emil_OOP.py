import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk

class Ansatt:
    def __init__(self, navn, lønn):
        self.navn = navn
        self.lønn = lønn

    def vis_info(self):
        return (f"Navn: {self.navn}, lønn: {self.lønn}")
    

class Lærer(Ansatt):
    def __init__(self, navn, lønn, fag):
        super().__init__(navn, lønn)
        self.fag = fag

    def vis_info(self):
        return (f"Navn: {self.navn}, lønn: {self.lønn}, fag: {self.fag}")
    

class Rektor(Lærer):
    def __init__(self, navn, lønn, fag):
        super().__init__(navn, lønn, fag)
        self.b = []

    def legg_liste(self, c):
        self.b.append(c)

    def lønnkostnad(self):
        sum_kostnad = 0
        for x in self.b:
            sum_kostnad += x.lønn

        sum_kostnad += self.lønn
        return sum_kostnad

     
p1 = Rektor("Danni", 530, "Matte")

print(p1.vis_info())

p2 = Lærer("fdfd", 42, "Nrsk")
p1.legg_liste(p2)

print(p1.lønnkostnad())

