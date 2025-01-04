import random as r
import turtle as t
import matplotlib.pyplot as plt
import numpy as np
from timeit import default_timer as timer
from datetime import timedelta
import itertools as it

### Problem 1

def natural_log_equation(x_value):
    y_value=(x_value)**3+np.log(x_value)
    return y_value
def equation_derivative(x_value):
    derivative=3*((x_value)**2)+(1/x_value)
    return derivative


def graph_only():
    set_x=[]
    set_y=[]
    for i in range(0,201):
        set_y.append(i/100)
        set_x.append(natural_log_equation(i/100))
    plt.scatter(set_y, set_x)
    plt.show()


def bisection_method():
    bisection_y=[]
    bisection_x=[]
    delta=10
    maximum=2
    minimum=0
    domain=1
    while delta > 0.00001:
        new=(maximum+minimum)/2
        delta=abs(natural_log_equation(new))
        if natural_log_equation(new)>0:
            maximum=new
        else:
            minimum=new
        bisection_y.append(abs(natural_log_equation(new)))
        bisection_x.append(domain)
        domain+=1
    return(bisection_x, bisection_y)

def newton_method():
    newton_x=[]
    newton_y=[]
    new = 1
    delta=abs(natural_log_equation(new))
    domain=1
    newton_x.append(domain)
    newton_y.append(delta)
    while delta > 0.00001:
        new=new-(natural_log_equation(new)/equation_derivative(new))
        # print(f'delta; {delta}, newest value; {new}')
        delta = abs(natural_log_equation(new))
        domain+=1
        newton_x.append(domain)
        newton_y.append(delta)
    return newton_x,newton_y
        


def comparison():
    bisection_x, bisection_y=bisection_method()
    newton_x, newton_y=newton_method()
    plt.plot(bisection_x, bisection_y, label="bisection method")
    plt.plot(newton_x, newton_y, label="newton method")
    plt.legend()
    plt.show()


#graph_only()
#bisection_method()
#newton_method()
#comparison()

## Problem 2
f=open("worddic.txt", "r")
dicL=f.read().splitlines()
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# print(len(dicL))

def alphabet_occurance():
    count=[]
    for i in range(26):
        count.append(0)
    for word in dicL:
        for letter in word:
            for character in range(26):
                if alphabet[character]==letter:
                    count[character]+=1
                    
    plt.bar(alphabet, count, width=1.0)
    # plt.show()
    return count
        

def entropy():
    count=alphabet_occurance()
    total_entropy=0
    all_letters=sum(count)
    probability_list=[]
    for i in range(26):
        per_occurance=(count[i]/all_letters)
        # calculating the entropy recieved on average per letter
        # this needs to be added up for all letters, then divided by 26
        # giving the average entropy per letter
        individual_entropy=per_occurance*np.emath.logn(26,per_occurance)*-1
        total_entropy+=individual_entropy
        probability_list.append(individual_entropy)
    # print(total_entropy/26)
    return probability_list

def distribution():
    ## want to repeat the most likely 1/26th chance of getting called
    probabilities=entropy()
    better=0
    delta=1
    all_averages=[]
    count=0
    for i in dicL:
        length=len(i)
        sum=0
        for char in i:
            for num in range(26):
                if alphabet[num]==char:
                    sum+=probabilities[num]
                    break
        all_averages.append(sum/length)
    for prob in all_averages:
        count+=1
        if prob>better:
            better=prob
            max_indices=count

    print(dicL[max_indices], all_averages[max_indices])
        
                    
        
        




# alphabet_occurance()
# entropy()
# distribution()


## Problem 3
def graphing_monte(dots):
    within=0
    for i in range(dots):
        x=r.random()
        y=r.random()
        if ((x**2+y**2)**(1/2))<1 and (((1-x)**2+(y)**2)**(1/2))<1:
            plt.scatter(x,y, color='green')
            within+=1
        else:
            plt.scatter(x,y, color='red')
    #plt.show()
    print(within)
    area=within/dots
    print(f'estimated area {area}')
    plt.show()

## with 10000, got 0.6131





# graphing_monte(10000)




# problem 4

def polygon_figure():
    points=int(input('number of points: '))
    skipped=int(input('connects number of points: '))
    t.speed(6)
    size=900
    inner_degree=360/points
    segment = size/points
    
    ## center cicle
    t.pd()
    center_radius=2
    t.teleport(0,-center_radius)
    t.seth(0)
    t.color('red')
    t.circle(center_radius)
    
    
    ## go to drawing outer location
    t.teleport((segment/2),(-size/np.pi)/2)
    t.seth(180)
    location_x=[]
    location_y=[]
    count=0
    for i in range(points):
        t.pu()
        t.color('black')
        location_x.append(t.xcor())
        location_y.append(t.ycor())
        t.fd(segment)
        t.right(inner_degree)
    
    x_extended=location_x*points
    y_extended=location_y*points
    
    for i in range(points+1):
        t.pd()
        t.goto(x_extended[count],y_extended[count])
        count+=skipped
    
    t.write(f'n= {points}, k={skipped}')

    
    t.done()


# polygon_figure()

## problem 5



def koch_snowflake(x_cord,y_cord):
    t.speed(9)
    n=int(input('level of n: '))
    ## full straight line is 200
    full=400
    h=(1-0.5**2)**(1/2)
    # x_cord=[-full/2,full/2]
    # y_cord=[0,0]
    count=1
    t.teleport(x_cord[0],y_cord[0])
    ## function for in between functions
    for i in range(n):
        if i==n-1:
            t.pd()
        else:
            t.pu()
        new_x=[]
        new_y=[]

        def add_pos():
            new_x.append(t.xcor())
            new_y.append(t.ycor())

        t.teleport(x_cord[0],y_cord[0])
        for i in range(len(x_cord)-1):
            segment=round((full/(3**count)), 4)
            add_pos()
            t.seth(t.towards(x_cord[i+1],y_cord[i+1]))
            t.fd(segment)
            add_pos()
            t.left(60)
            t.fd(segment)
            add_pos()
            t.right(120)
            t.fd(segment)
            add_pos()
            t.left(60)
            t.fd(segment)
        add_pos()
        x_cord=new_x
        y_cord=new_y
        count+=1
        print(x_cord, y_cord)
    t.done()
    
    
def star_koch():
    bottom=(400**2-200**2)**(1/2)
    star_x=[-200,200,0,-200]
    star_y=[0,0,-bottom,0]
    koch_snowflake(star_x,star_y)






#koch_snowflake()
#star_koch()

## Problem 6
f=open("all_pandigital.txt", "r")
all_pan=f.read().splitlines()

def small_pan():
    

    '''# Generate all permutations of the digits 0 to 9
    numbers = "0123456789"
    possible = [''.join(i) for i in it.permutations(numbers)]
    print(f'done generating overallist {len(possible)} ')

    f = open("all_pandigital.txt", "w")

    for x in possible:
        if x[0]!='0':
            print(x, file=f)
        
    f.close'''

    print(all_pan[:5])

def divisible():
    f = open("divisible.txt", "w")
    passed=[]
    for i in all_pan:
        now=True
        q=int(i)
        for n in range(1,10):
            if q%n!=0:
                now=False
                break

        if now==True:
            print(i, file=f)
        
    f.close

def square():
    square=[]
    for pan in all_pan:
        root=(int(pan)**0.5)
        if root%1==0:
            square.append(pan)
            print(f'found {pan}, root {root}')

    print(len(square))


def square_fancy():
    square=[]
    for num in range(30000, 100000):
        sq=num**2
        now=True
        for div in range(0,10):
            if str(div) not in str(sq):
                now=False
                break
        if now==True:
            square.append(num**2)
    print(len(square))



#small_pan()
#divisible()
#square()
square_fancy()