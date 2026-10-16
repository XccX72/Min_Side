import sympy as sp
from sympy import Eq, Abs, Sum, symbols, diff, simplify,expand,factor,solve,limit,sin


#----------------------Symbols()------------------------#
"""
Lager symboler som kan brukes som mattematiske variabler
f. eks. som x eller y i en vanlig matte oppgave
"""

x = sp.symbols('x')  
f = x**2 + 3*x + 2
print(f)

#-----------------------Subs()-----------------------#
"""
Subs som er short for substitute/erstatt, erstatter et 
symbol med en verdi eller et annet utrykk 
"""

f = x**2 + 3*x + 2
verdi = f.subs(x, 5)  
print(verdi)

#-----------------------Solve()-----------------------#
"""
Solve tar et utrykk og finner ut hva symbolet/variabelen
må være for at utrykket skal bli 0. F. eks. solve(utrykk,x)
der utrykk er utrykket du skal sette lik 0 og x er symbolet
"""

ligning = x**2 - 4
losning = sp.solve(ligning, x)
print(losning)

#-----------------------Diff()-----------------------#
"""
Diff er funkjsonen for deriver. Den deriverer et utrykk
med hensyn til en variabel. Grunnleggende syntaks er:
sp.diff(uttrykk, symbol) der uttrykk er funksjonen du vil
derivere og symbol er variabelen du derivere med hensyn til.
"""

x = symbols('x')
f = x**2 + 3*x + 2
df = diff(f, x)
print(df)

#------------------------Limit()----------------------#
"""
Beregner grenseverdien av et symbolsk uttrykk når en variabel nærmer seg et punkt.
Kan brukes til å finne grenser som i kalkulus (f.eks. lim x->0 sin(x)/x = 1).
"""

x = symbols('x')
f = sin(x)/x
grense = limit(f, x, 0)  # grense når x går mot 0
print(grense)  # 1


#------------------------Simplify()-------------------#
"""
Forenkler et uttrykk symbolsk til en enklere form.
Kan kombinere brøker, faktorer og like ledd.
"""

from sympy import symbols, simplify
x = symbols('x')
f = (x**2 - 1)/(x - 1)
print(simplify(f))  

#------------------------Expand()---------------------#
"""
Utvider produkter og parenteser i algebraiske uttrykk.
Gjør f.eks. (x+1)**2 om til x^2 + 2*x + 1
"""

from sympy import expand
x = symbols('x')
f = (x + 1)**2
print(expand(f))  

#------------------------Factor()---------------------#
"""
Faktorisering av polynomer eller algebraiske uttrykk.
Deler opp uttrykk i produkt av enklere faktorer.
"""

from sympy import factor
x = symbols('x')
f = x**2 + 2*x + 1
print(factor(f))  

#------------------------Eq()-------------------------#
"""
Lager en symbolsk ligning som kan brukes sammen med solve.
f.eks. x^2 - 4 = 0 som en objektorientert ligning.
"""

x = symbols('x')
ligning = Eq(x**2 - 4, 0)
losning = solve(ligning, x)
print(losning) 

#------------------------Sum()------------------------#
"""
Symbolsk sum-funksjon, summerer et uttrykk over et gitt intervall.
Kan brukes som Σ i matematikk.
"""

x = symbols('x')
f = Sum(x, (x, 1, 5))  
print(f.doit())  

#------------------------Abs()------------------------#
"""
Absoluttverdi-funksjon, finner alltid den positive verdien
av et tall eller symbolsk uttrykk.
"""

x = symbols('x')
f = Abs(-5)
print(f)  # 5

