import random as r
import turtle as t
import matplotlib.pyplot as plt
import numpy as np
from timeit import default_timer as timer
from datetime import timedelta

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
    new = 2
    delta=abs(natural_log_equation(new))
    domain=1
    while delta > 0.0001:
        new=new-(natural_log_equation(new)/equation_derivative(new))
        # print(f'delta; {delta}, newest value; {new}')
        delta = abs(natural_log_equation(new))
        newton_x.append(domain)
        domain+=1
        newton_y.append(delta)
    return newton_x,newton_y
        


def comparison():
    bisection_x, bisection_y=bisection_method()
    newton_x, newton_y=newton_method()
    plt.plot(bisection_x, bisection_y, label="bisection method")
    plt.plot(newton_x, newton_y, label="newton method")
    plt.legend()
    plt.show()

### Problem 1
graph_only()
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
    return count
    # plt.show()        
        

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
        
                    
        
        



### Problem 2
#alphabet_occurance()
#entropy()
#distribution()

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

## with 10000, got 0.6131




## Problem 3
# graphing_monte(10000)




# problem 4