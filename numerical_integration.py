import random as rd
import matplotlib.pyplot as plt
import numpy as np
import math as m

n=1000000
xmin=0
xmax=1


#function that I want to numerically integrate
def function(x):
    return 


#partitions an interval into little pieces then returns the list 
def partition(xmin,xmax,n):
    sample_points=[]
    lenght=xmax-xmin
    for i in range(0,n+1):
        a= xmin + (float(lenght)*float(i)/float(n))
        sample_points.append(a)

    return sample_points

#a list that has the values of the function at sample point in the partition
#interval

#height function that returns a list of the heights of f

def heightfunction():
    height=[]
    for i in partition(xmin,xmax,n):

        u=function(i)
        height.append(u)

    return height

#gives height of function

#area of rectangle function



#area of each little rectangle of the function

def list_of_areas(height_list,base_list):
    area_list=[]
    for i in range(n):
        base = (base_list[i+1]-base_list[i])
        area = base * (height_list[i+1] + height_list[i])/2
        area_list.append(area)

    return area_list


        




def numerical_integration(my_list):
    total=sum(my_list)
    return total

value=(numerical_integration(list_of_areas(heightfunction(),partition(xmin,xmax,n))))



print(value*4)
    
        






        


        



        




