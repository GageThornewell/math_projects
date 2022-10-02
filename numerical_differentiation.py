import random as rd
import matplotlib.pyplot as plt
import numpy as np
import math as m

n = 10000 # partition
a = -4*m.pi #lower point of interval
b= 4*m.pi #upper point of interval


def func(x): # function you want to numerically differentiate
    return m.sin(x)

def differentiate(x):
    
    h = 1.0*10**-6
    diff_quot = (func(x)-func(x+h))/h

    return diff_quot

interval = np.linspace(a,b,n)

function=[]
derivative=[]

for i in interval:
    function.append(func(i))
    derivative.append(differentiate(i))


#plot for the numerical differentiation of function
plt.plot(interval,function,label="function")
plt.plot(interval,derivative,label="derivative of function")
plt.title("Numerical Differentiation of Function")
plt.ylabel("return value of function and derivative")
plt.xlabel("x values from  " + str(a) + " to " + str(b))
plt.grid()        #grid
plt.legend(loc=1) #legend

plt.show()




    

    
