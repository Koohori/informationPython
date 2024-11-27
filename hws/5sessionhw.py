import turtle as t
from random import random


t.speed(0)
len=30

def square(a):

    for i in range(4):
        t.left(90)
        t.forward(a)




for num in range(1,6):
    if num%3==1:
        t.color('red')
    elif num%3==2:
        t.color('blue')
    else:
        t.color('yellow')
    square(len)
    t.right(90)
    t.penup()
    t.fd(100)
    t.pendown()

t.done()
