import random as rnd


#--- Velge bare partall i en liste av int -----

a = [1, 4, 5, 2, 6, 8, ]

def filtrer_partall(a):
    b = []
    for i in a:
        if i % 2 == 0:
            b.append(i)
        else:
            continue
    
    return (b)

print(filtrer_partall(a))

# ---- 

b = (input("Skriv noe")).lower()

def tell_ord(b):
        c = {}
        ab = [str(s) for s in b.split()]
        a = max(len(b))
        c.appen()
        return b

print(tell_ord(b))