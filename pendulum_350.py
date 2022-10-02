
#Thomas and Gage - Pendulum experiment part 1 


import qexpy as q 
import math as m 
import numpy as np



m = q.Measurement(1061.12,0.01)/1000 #mass of pendulum , in grams 
r = q.Measurement(10.17,0.01)/100 #diameter of disk , in centimeters.      #multiplication factors are to convert to 
l = q.Measurement(24.10,0.002) *0.0254   #lenght of rod ,  in inches      # standard SI units

g = 9.8 # m/s^2 gravitational constant

I = m*l**2
T = 2* np.pi * (l/g)**(1/2) #period of oscilation 


# we think that we only need an error of half a second , 0.2 seconds because 
Period1 = q.MeasurementArray([1.38,1.34,1.43,1.38,1.38,1.41,1.37,1.43,1.34,1.44], error=0.2, units='s') #period of oscilation

print(T)