import random as rd
import matplotlib.pyplot as plt
import numpy as np
import math as m


#run as default to see the numerical and the approximation sinx = x solutions of the equation of motion of a pendulum. 
#also we can see a plot in error or the difference between numerical and the approximation. 


a = 0 # initial time
b = 60 # final time 
c = 1000 # thiness of time domain  #10000 points and r = 0.45 seem to give the most accurate
r = 0.45 # precision of algorithm
g = 9.81 #m/s^2
#l = 1.0 #meter's
t = 0  #degrees 
tdot = 0 #initial velocity in m/s 



I_small = 3.0 #current in small coil
R_small = 0.0762 #m
b_small = 0.0254 #m
n_small = 50
m_shaft = 0.0325 #kg
r_shaft = 0.0047625 #metres


I_large = 1.5  #current in large coil 
R_large = 0.127 # m 
b_large = 0.0508 # m 
n_large = 60
m_disk = 0.08352 #kg
r_disk = 3.17/100 #metres

I = 1/2*m_disk*r_disk**2 + 1/2*m_shaft*r_shaft**2 
muo = 1.25664*10**(-6) #permiattibility of free space

wd = 0.01 #frequency 

mu = 1 #magnetic dipole ? 



B_small = muo*n_small*I_small*R_small**2/(R_small**2 + b_small**2)**(1/2)

B_large = muo*n_large*I_large*R_large**2/(R_large**2 + b_large**2)**(1/2)

#print(B_small * mu)
#print(B_small)
print(B_large)

def f(t,x_1,x_2):
	return x_2

def h(t,x_1,x_2):
	return  (2)*(1*np.sin(x_1) + 1*np.sin(wd*t)*np.cos(x_1))



time = np.linspace(a,b,c) # interval of time which we wish to study the problem

x = np.zeros([c]) #solutions to x_1 
x[0] = (t) 

y = np.zeros([c]) #solutions to x_2
y[0] = (tdot)

#functions required to use the Runge kutta approximations

def kn1(t,x_1,x_2):
	x = f(t,x_1,x_2)
	y = h(t,x_1,x_2)

	return((x,y))

def kn2(t,x_1,x_2):
	x = f(t + (float(r/2)),x_1 + float(r/2) * (kn1(t,x_1,x_2)[0]) ,x_2 + float(r/2) * (kn1(t,x_1,x_2)[1]) )
	y = h(t + (float(r/2)),x_1 + float(r/2) * (kn1(t,x_1,x_2)[0]) ,x_2 + float(r/2) * (kn1(t,x_1,x_2)[1]) )
	
	return((x,y))


def kn3(t,x_1,x_2):
	x = f(t + (float(r/2)),x_1 + float(r/2) * (kn2(t,x_1,x_2)[0]) ,x_2 + float(r/2) * (kn2(t,x_1,x_2)[1]) )
	y = h(t + (float(r/2)),x_1 + float(r/2) * (kn2(t,x_1,x_2)[0]) ,x_2 + float(r/2) * (kn2(t,x_1,x_2)[1]) )
	
	return((x,y))

def kn4(t,x_1,x_2):
	x = f(t + r ,x_1 + r * (kn3(t,x_1,x_2)[0]) ,x_2 + r * (kn3(t,x_1,x_2)[1]) )
	y = h(t + r ,x_1 + r * (kn3(t,x_1,x_2)[0]) ,x_2 + r * (kn3(t,x_1,x_2)[1]) )
	
	return((x,y))


#numerically solves for x_1(i) and x_2(i) using initial conditions and funtions above. 


for i in range(1,c):
	x[i] = x[i-1] + float(r/6) * (kn1(time[i-1],x[i-1],y[i-1])[0] + 2*kn2(time[i-1],x[i-1],y[i-1])[0] + 
		   2*kn3(time[i-1],x[i-1],y[i-1])[0] + kn4(time[i-1],x[i-1],y[i-1])[0]) 
	y[i] = y[i-1] + float(r/6) * (kn1(time[i-1],x[i-1],y[i-1])[1] + 2*kn2(time[i-1],x[i-1],y[i-1])[1] + 
		   2*kn3(time[i-1],x[i-1],y[i-1])[1] + kn4(time[i-1],x[i-1],y[i-1])[1])



#solution using the approximation sinx = x 

#def Approx(o):
#	return t * m.cos(m.sqrt(float(l/g)) * o)


#approximation = [] 

#for i in time:
#	approximation.append(Approx(i))


#plots of curves and error curves. # to view angular velocities , replace x with y via via everything. 
'''
#plt.plot(time,approximation,label = 'Approximation ')
plt.plot(x,y,label = 'Numerical Exact')
plt.title('Phase Diagram - frequency 0.42rad/s')
plt.xlabel('angle (rad)')
plt.ylabel('angular velocity (rad/s)')
plt.legend(loc = 1)
plt.show()



difference = [] 
for i in range(0,c):
	v = abs(x[i]) - abs(approximation[i])
	difference.append(abs(v))

plt.plot(time,difference,label = 'Exact - Approximation')
plt.title('Error in Numerical and Approximation Solution')
plt.xlabel('Time  (seconds)')
plt.ylabel('Error ')
plt.legend(loc = 1)
plt.show()
'''






