import random as rnd
import math
import numpy as np

telling = np.zeros(11)

for i in range(1000000):
    t1 = rnd.randint(1,6)
    t2 = rnd.randint(1,6)
    telling[t1+t2-2] += 1

print (telling/10000)


