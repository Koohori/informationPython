import random as r
import turtle as t
import matplotlib.pyplot as plt
import numpy as np
from timeit import default_timer as timer
from datetime import timedelta


def fibn_interation():
    number=int(input('fibonaci until:'))
    fibn_list=[0]
    for i in range (1,number+1):
        x=i+fibn_list[-1]
        fibn_list.append(x)
    print(fibn_list[-1])

fibn_interation()