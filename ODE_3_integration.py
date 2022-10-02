
import random as rd
import matplotlib.pyplot as plt
import numpy as np
import math as m


 # ODE to solve
def f(t,y):
	return 1 - t + 4*y 


def numerical_integrate(a,b,n,p):

    partition=[]
    height=[]
    areas=[]
    lenght = b-a  #lenght of interval 


    for i in range(0,n+1):
        delta_x = a + (float(lenght)*float(i)/float(n)) #makes partition
        partition.append(delta_x)

    for j in partition:
        u = (f(j,p) + f(j-1,p) ) / 2         #finds height of function at partition values
        height.append(u)  


    for k in range(n):
        base = partition[k+1]-partition[k]
        area = base*height[k]               #finds area using midpoint rectangles ( converges faster)
        areas.append(area)

    

    total = sum(areas)

    if total > -0.000001 and total < 0.000001:
        return 0



    else:
        return total

  


#x0 = lower interval bound
#xf = upper interval bound
#y0 = initial condition
#n = number of steps    

def Euler(x0,xf,y0,n):
	vectors = []
	x = np.linspace(x0,xf,n)
	y = np.zeros([n])
    	y[0] = y0

    	for i in range(1,n):
			y[i] = y[i-1] + numerical_integrate(x[i-1],x[i],100,y[i-1]) #integration interval doesnt have to be so 
    																	 # large since n is large
	for i,j in zip(x,y):
		a = (i,j)
		vectors.append(a)

	return vectors

#print(Euler(0,2,1,1000))


### making the list of point for the exact solution 
################################
x = np.linspace(0,2,100)
interval_1 = [] 

def a(t):
    return  1/4*t - 3/16  + 19/16 * np.exp(4*t)


for i in x:
    c = a(i)
    interval_1.append(c)
#############################

plt.plot(x,interval_1,label = 'Exact')
plt.plot(*zip(*Euler(0,2,1,1000000)), label = 'Numerical')
plt.title("Comparison of Exact Solution and Numerical Solution")
plt.xlabel('x-values')
plt.ylabel('Output')
plt.legend()
plt.show()



  




