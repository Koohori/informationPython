import random as r
import turtle as t


t.speed(0)

triangles = int(input('number of triangles: '))

def triangle():
    for i in range(3):
        t.fd(30)
        t.left(120)

xcordinates = []
ycordinates = []

for i in range(triangles):
    x=r.randint(-300,300)
    y=r.randint(-300,300)
    t.color('blue')
    t.pu()
    t.goto(x,y)
    t.pd()
    triangle()
    xcordinates.append(x)
    ycordinates.append(y)

print(xcordinates)
print(ycordinates)

for i in range(triangles):
    t.color('red')
    t.pd()
    t.goto(xcordinates[i],ycordinates[i])
t.goto(0,0)





t.pd()
t.done()






"""


def star(b):
    for i in range(1,6):
        t.pd()
        t.fd(b)
        t.left(144)


def square(a):
    for i in range(4):
        t.pu()
        t.left(90)
        t.forward(a)
        ang=t.heading()
        t.setheading(0)
        star(len)
        t.setheading(ang)



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
"""
