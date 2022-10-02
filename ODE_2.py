import random as rd
import matplotlib.pyplot as plt
import numpy as np
import math as m


x0 = 0
xf = 3
y0 = 1 
n = 1000000
h = (xf-x0)/float(n)

x = np.linspace(x0,xf,n)
y = np.zeros([n])
y[0] = y0

 # ODE to solve
def f(t,y):
	return 1 - t + 4*y 

for i in range(1,n):
	y[i] = (h * (f(x[i-1],y[i-1])) + y[i-1])


label = 'Exact'




#actual solution

def a(t):
    return  1/4*t - 3/16  + 19/16 * np.exp(4*t)

interval_1 = []

for i in x:
    c = a(i)
    interval_1.append(c)

plt.plot(x,interval_1,)
plt.plot(x,y, label = 'Numerical')
plt.title("Comparison of Exact Solution and Numerical Solution")
plt.xlabel('x-values')
plt.ylabel('Output')
plt.legend()
plt.show()


difference=[]
for i in range(0,n):
	a = interval_1[i] - y[i]
	difference.append(a)

plt.plot(x,difference)
plt.title("Difference Between Exact and Numerical solutions")
plt.xlabel('x-values')
plt.ylabel('Difference')
plt.show()


