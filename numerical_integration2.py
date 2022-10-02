'''
import random as rd
import matplotlib.pyplot as plt
import numpy as np
import math as m




#function to be used in numerical integration
a=2
b=1

def function(x):
    return np.sqrt(a**2 * m.sin(x)**2 + b**2 * m.cos(x)**2)


#numerical integration function and depends on parameters
# a = lower integration limit
# b = upper integration limit
# n = finess of partition 

def numerical_integrate(a,b,n):

    partition=[]
    height=[]
    areas=[]
    lenght = b-a  #lenght of interval 


    for i in range(0,n+1):
        delta_x = a + (float(lenght)*float(i)/float(n)) #makes partition
        partition.append(delta_x)

    for j in partition:
        u= (function(j) + function(j-1) ) / 2         #finds height of function at partition values
        height.append(u)  


    for k in range(n):
        base = partition[k+1]-partition[k]
        area = base*height[k]               #finds area using midpoint  rectangles
        areas.append(area)

    

    total = sum(areas)

    if total > -0.000001 and total < 0.000001:
        return 0



    else:
        return total


#print( 'the area is' ,numerical_integrate(0,2*m.pi,100000))




time = linspace(0,2*m.pi,1000):

arc_length = [] 

for i in range(0,999):
	numerical_integrate(0,2*m.pi,100000)



'''

#import the module
import qexpy as q
#declare 2 Measurements, x and y
x = q.Measurement(10,1)
y = q.Measurement(5,3)
#define a quantity that depends on x and y:
z = (x+y)/(x-y)
#print z, with the correct error
print(z)








    



        







        
