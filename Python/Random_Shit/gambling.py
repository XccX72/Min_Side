import math
import numpy
import random as rnd
 
def is_even(a):
    if a % 2 == 0:
        return True
    else:
        return False
    

print(is_even(4))

def calculate_caverage(liste):
    if len(liste) == (0):
         return 0
    else:
        vlfk = sum(liste)
        dgd = len(liste)
        dfdf = vlfk/dgd
        return dfdf

print(calculate_caverage([1, 3, 4]))

print(calculate_caverage([]))

def sort_list_descending(tallmengde):
    for i in range(len(tallmengde)):
        for j in range(0, len(tallmengde) - i -1):
             if tallmengde[j] < tallmengde[j +1]:
                  tallmengde[j], tallmengde[j + 1] = tallmengde[j + 1], tallmengde[j]
    return tallmengde
          
print(sort_list_descending([1462,522,6,47,3,72,73583,1,73,6,3,63,7,3]))

for i in range(1, 4):
     for j in range(13):
          print(f"i={i} og j={j}")

for i in range(1,5):
    if i == 3:
        print(3)
        break   # hopper over 3
    print(i)




