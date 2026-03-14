#Øving på Python 9.9.10

import math
import random as rnd

#forr løkke som lager 10 random tall
#rnd er bib og random er funksjonen i bib
#Uten *6 blir det bare mellome [0, 6>
for i in range(0):
    print(rnd.random()*6)

#Round gjør om til heltall, 1 er antall desimaler
for i in range(10):
    print(round(rnd.random()*6))
#ceil runder oppover
#Begge gjør samme ting
for i in range(10):
    print(math.ceil(rnd.random()*6))
    print(rnd.randint(1, 6))

#Guess the number spill
for i in range (1000):
    print(rnd.random())