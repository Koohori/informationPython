import turtle as t
import random as r
import matplotlib.pyplot as plt
import numpy as np




def divisorsum(n):
    div_sum=0
    for i in range(1,n+1):
        if n%i==0:
            div_sum+=i
    return(div_sum)

def find_range_perfect():
    finding = []
    for i in range(1,10001):
        if 2*i == divisorsum(i):
            print(i)
            finding.append(i)
    print(finding)

def find_all_perfect():
    all_perfect=[]
    for i in range(1,50001):
        factor=1
        sum = divisorsum(i)
        while factor*i < sum:
            factor+=1
        ## print(sum*factor, factor, i)
        if factor*i==sum:
            all_perfect.append(i)
            print(all_perfect)
    print(all_perfect)

def separated_next_finder():
    next_perfect =[]
    current = 50000
    while True:
        print(current)
        divisor=[]
        low=1
        high=current
        while low < high:
            if current%low==0:
                high=current/low
                divisor.extend([low,high])
            low+=1
        if sum(divisor)%current==0:
            print(divisor, sum(divisor),current )
            return(current)
        else:
            current+=1

    print(divisor)


        


    

# problem 1
#divisorsum(int(input('Sum of devisors for the number: ')))
#find_range_perfect()
# find_all_perfect()
#separated_next_finder()


def isprime(n):
    for i in range(2,n):
        if n%i==0:
            return False
            break
    else:
        return True

def prime_lists():
    prime_list = [i for i in range (2,101) if isprime(i) is True]
    # print(prime_list)
    return(prime_list)

def gc():
    for i in range(4,101):
        if i%2==0:
            for x in prime_lists():
                for y in prime_lists():
                    if x+y==i and x>=y:
                        print(f'{i} can be made from {x} + {y}')


def pair_prime_finder(n):
    if n > 10000:
        print('number too big, must be less than 10000')
    prime_list = [i for i in range (2,n) if isprime(i) is True]
    for x in prime_list:
                for y in prime_list:
                    if x+y==n and x>=y:
                        print(f'{n} can be made from {x} + {y}')

# question 2
# print(isprime(int(input('number is either prime or not prime: '))))
#prime_lists()
#gc()
# pair_prime_finder(int(input('pairs for the number: ')))

def findloner_without_xor():
    l=[5,67,34,67,2,5,34]
    for number in l:
        if l.count(number) == 1:
            print(f'{number} is the outlier within the list')


def findloner_with_xor():
    l=[5,67,34,67,2,5,34,48,12,2]
    result = 0
    for num in l:
        print(num, result)
        result^=num
    print(result)


    ''' length=len(l)
    for x in range (length):
        test=False
        for y in range(length):
            if x!=y:
                if l[x]^l[y]==0:
                    test = True
                    break
                    
        if test != True:
            print(f'{l[x]} is the outlier') '''
            
            
# question 3
#findloner_without_xor()
# findloner_with_xor()

import turtle as t

def colorful_circle():
    t.bgcolor('black')
    t.speed(0)
    sides=1
    for i in range(1,12):
        for x in range(30):
            t.fd(sides)
            t.left(12)
            if x%5==0:
                t.color('red')
            elif x%5==1:
                t.color('blue')
            elif x%5==2:
                t.color('green')
            elif x%5 == 3:
                t.color('purple')
            elif x%5==4:
                t.color('pink')
            else:
                t.color('yellow')
            sides+=0.2
        

    t.done()
# question 4
# colorful_circle()

def happy_list_function(n):
    list=[n]
    test = False
    cal=0
    for i in range(len(n)):
        cal+=int(n[i])**2
    next_num=str(cal)
    list.append(next_num)
    # print(list)


    while next_num != '1' and test==False:
        cal=0
        for i in range(len(next_num)):
            cal+=int(next_num[i])**2
        next_num=str(cal)
        list.append(next_num)

        # print(list)

        length=len(list)
        result = 0
        for x in range (length):
            test=False
            for y in range(length):
                if x!=y:
                    if int(list[x])^int(list[y])==0:
                        test = True
    # print(f'last digit: {list[x]}')
    if list[-1] == '1':
        print(list)
        print(f'for {n}, last calculated number {next_num}')
        return True
    else:
        print(list)
        print(f'for {n}, last calculated number {next_num}')
        return False

def happpy_numbers_within(upper):
    under_k=[]
    count = 0
    for i in range (1,upper):
        if happy_list_function(str(i)) is True:
            under_k.append(int(i))
            count +=1
    print(f'between 1 and {upper-1}, there are {count} happy numbers')
    return under_k
            
def plt_happy_num():
    
    y=[]
    for i in range(142):
        y.append(1)
    print(len(y))

    x=happpy_numbers_within(1000)
    print(x)
    ally=[v for v in range(1000)]
    allx=[1 for v in range(1000)]
    plt.plot(x,y,'o')
    plt.plot(ally,allx,'-')
    plt.show()
    
    
    
    
## problem 5
#happy_list_function(input('potential happy list for: '))
#happpy_numbers_within(int(input('find the number of happy nums under: ')))
''' comment for happiness rate
below 100: 19
below 1000: 142
below 10^6: 143760
'''
# plt_happy_num()


def rand_triangles():
    
    t.color('blue')
    t.speed(0)
    for x in range(6):
        heading=r.randint(0,360)
        side=r.randint(1,200)
        x_pos=r.randint(-250,250)
        y_pos=r.randint(-250, 250)
        diag=((((side/2)**2+side**2))**(1/2))/2
        t.teleport(x_pos,y_pos)
        t.setheading(heading)
        t.color('blue')
        for i in range(3):
            t.forward(side)
            t.right(120)
        t.right(30)
        t.color('red')
        t.pu()
        t.fd(diag)
        t.fd(side)
        t.pd()
        t.left(90)
        t.circle(side)
        

    t.done()



def rand_squares():
    t.color('blue')
    for x in range(6):
        heading=r.randint(0,360)
        side=r.randint(1,200)
        x_pos=r.randint(-250,250)
        y_pos=r.randint(-250, 250)
        diag=(((2*(side**2))**(1/2))/2)
        t.teleport(x_pos,y_pos)
        t.setheading(heading)
        t.color('blue')
        for i in range(4):
            t.forward(side)
            t.right(90)
        t.right(45)
        t.color('red')
        t.pu()
        t.fd(diag)
        t.fd(side)
        t.pd()
        t.left(90)
        t.circle(side)
    t.done()

def polygons(points):
    t.color('blue')
    for x in range(6):
        heading=r.randint(0,360)
        side=r.randint(1,200)
        x_pos=r.randint(-250,250)
        y_pos=r.randint(-250, 250)
        diag=(((2*(side**2))**(1/2))/2)
        t.teleport(x_pos,y_pos)
        t.setheading(heading)
        t.color('blue')
        turn=360/points
        xcord=[]
        ycord=[]
        for i in range(points):
            xcord.append(t.xcor())
            ycord.append(t.ycor())
            t.right(turn)
            t.fd(side)
        xtele=sum(xcord)/points
        ytele=sum(ycord)/points
        t.teleport(xtele,ytele)
        t.color('red')
        t.pu()
        t.forward(side)
        t.pd()
        t.left(90)
        t.circle(side)
    t.done()
            
            


t.speed(0)

# rand_triangles()
# rand_squares()
polygons(int(input('degree of pollygon:')))
            
        

