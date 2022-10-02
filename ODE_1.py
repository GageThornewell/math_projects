import random as rd
import matplotlib.pyplot as plt
import numpy as np
import math as m

n = 100
step = 1/n
#solution to the first order differential equation
def a(t):
    return  1/4*t - 3/16  + 19/16 * np.exp(4*t)

time = np.linspace(0,1,n)
interval_1 = []

for i in time:
    c = a(i)
    interval_1.append(c)



def f(t,y):
	return 1 - t + 4*y   

#code for the solution of the differential equation

y_o = 1  #initial condition


y = np.zeros([n])
y[0] = y_o


for i in range(1,n): 
	y[i] = (y[i-1]) +  step * f(time[i-1],y[i-1])

print(y)

	

	


	



'''


plt.plot(time,interval_1,label = 'Exact')
plt.plot(time,y,'o', label = 'Numerical')
plt.title("Comparison of Exact Solution and Numerical Solution")
plt.xlabel('Time Domain')
plt.ylabel('Output')
plt.legend()
plt.show()


'''







