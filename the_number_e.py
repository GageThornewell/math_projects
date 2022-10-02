import random as rd
import matplotlib.pyplot as plt
import numpy as np
import math as m



def factorial(n):
    num = 1
    while n>= 1:
        num = num * n
        n = n -1
    return num


def approx_e(n):
    sequence=[]
    for i in range(n):
        term= float(1)/float(factorial(i))
        sequence.append(term)

    print("e is approximately equal to ",  sum(sequence))

approx_e(100)

            
