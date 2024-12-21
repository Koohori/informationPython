import random as r
import turtle as t
import matplotlib.pyplot as plt
import numpy as np
from timeit import default_timer as timer
from datetime import timedelta



def plotting_graph():
    plot_x=[]
    plot_y=[]
    for i in range(1,401):
        plot_x.append(i)
        plot_y.append(((i*0.01)**2)-5)
        
    plt.plot(plot_x,plot_y)
    plt.show()

def bisection_method():
    # assume that it is somewhat close to 2.5, which is half of 5
    # the value could be both overhot and undershot
    current=2.5
    lower_bound=1
    upper_bound=4
    delta=current**2-2
    cycle=0
    cycle_plot=[]
    delta_plot=[]

    # while delta >= 0.1 or delta <= 0.1:
    while abs(delta) >= 0.00001:
        if delta > 0.00001: 
            upper_bound=current
            current=(current+lower_bound)/2
            
        elif delta < 0.00001:
            lower_bound=current
            current=(current+upper_bound)/2
        else:
            print(current)
            break
        
        delta=current**2-2
        cycle+=1
        print(cycle, delta, current)
        cycle_plot.append(cycle)
        delta_plot.append(delta)
    print(cycle_plot, delta_plot)
    return cycle_plot, delta_plot

def graphing_iteration():
    cycle_plot, delta_plot = bisection_method()
    plt.bar(cycle_plot, delta_plot)
    plt.show()

## pir2/4 ;  r^2
## p0ints in : total

def finding_pi(iterations):
    ix_plot=[]
    iy_plot=[]
    ox_plot=[]
    oy_plot=[]
    count=0
    for i in range(iterations):
        x=r.random()
        y=r.random()
        distance=((x)**2+(y)**2)**(1/2)
        if distance <= 1:
            count+=1
            ix_plot.append(x)
            iy_plot.append(y)
        else:
            ox_plot.append(x)
            oy_plot.append(y)
    print(f'Pi roughtly should equal to: {count/iterations*4}')
    plt.scatter(ix_plot, iy_plot, color='blue')
    plt.scatter(ox_plot, oy_plot, color='red') 
    plt.show()



#plotting_graph()
#bisection_method()
#graphing_iteration()
finding_pi(9000)