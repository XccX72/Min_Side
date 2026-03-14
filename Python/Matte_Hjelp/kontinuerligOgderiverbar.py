import sympy as sp
import math

a = sp.symbols('a')
x = sp.symbols('x')

################
f1 = 0.11*x
f2 = 1/x
################

kontinuitet = sp.solve(f1.subs(x, a) - f2.subs(x, a), a)


deriverbar = []
for punkt in kontinuitet:
    f1Deri = sp.diff(f1, x).subs(x, punkt)
    f2Deri = sp.diff(f2, x).subs(x, punkt)
    
    if f2Deri == f1Deri:
        deriverbar.append(punkt)

#----------------------------------------------------------------------#

print("-"*40)

if len(kontinuitet)== 0:
    print(f"\n f(x) er ikke kontinuerlig\n")
else:
    for punkt in kontinuitet:
        print(f"\nf(x) er kontinuerlig i punktet {punkt:.0f}\n")

if len(deriverbar)== 0:
    print(f"\n f(x) er ikke deriverbar")
else:
    for punkt in deriverbar:
        print(f"\nf(x) er deriverbar i punktet {punkt:0f}\n")

print("-"*40)
