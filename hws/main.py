'''import random as r
import turtle as t
import matplotlib.pyplot as plt
import numpy as np
from timeit import default_timer as timer
from datetime import timedelta


def pi_monte_caro():
    result=0
    current_denom=-1
    for i in range(9000000):
        current_denom+=2
        if i%2 == 1:
            result-=(4/current_denom)
        else:
            result+=(4/current_denom)
        print(result)
    print(result)

'''

# pi_monte_caro()


q=1234567890
now=True
for n in range(1,10):
    print(n)
    if q%n!=0:
        now=False

if now==True:
    print(q,now)