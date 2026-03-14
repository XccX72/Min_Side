import math

a = -20
b = 20
noy = 0.001

def f(x):
    return (x**2-4*x+3) /(x-2)

m = (a+b)/2

while abs(f(m)) >= noy:
    if f(a)*f(m) < 0:
        b=m 
    else:
        a = m

    m = (a+b)/2

print("sdfghj", round(m, 4))