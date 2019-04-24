# -*- coding: utf-8 -*-
#Python 2.7 Anaconda 2
"""


"""
#=======================================================
#                   Problem 1
#=======================================================
import numpy as np
#In class problem number 1 my way
print 'Problem 1'
sum1 = 0
for i in range(1,10+1,1):
    sum1 = sum1 + 5*(i)
print 'The sum of the series is =', round(sum1,2)

#Problem 1 Huazhi way
total = 0

for i in range(1, 11):
    term = 5 * i
    total = total + term
    
    print ('term:' + str(term))

print (total)

#=======================================================
#                   Problem 2
#=======================================================
print 'Problem 2'
total = 0
n = 10
n1 = 50
n2 = 100
n3 = 1000

for i in range(n+1):
    term = 8*((4*i+1)*(4*i+3))**-1
    total = total + term
    
    #print ('term:' + str(term))

print (total)
print (np.pi-total)

for i in range(n1+1):
    term = 8*((4*i+1)*(4*i+3))**-1
    total = total + term
    
    #print ('term:' + str(term))

print (total)
print (np.pi-total)
for i in range(n2+1):
    term = 8*((4*i+1)*(4*i+3))**-1
    total = total + term
    
    #print ('term:' + str(term))

print (total)
print (np.pi-total)
for i in range(n3+1):
    term = 8*((4*i+1)*(4*i+3))**-1
    total = total + term
    
    #print ('term:' + str(term))

print (total)
print (np.pi-total)

#=======================================================
#                   Problem 3
#=======================================================
# Program for computing the height of a ball in vertical motion
print 'Problem 3'
#hello # The error is that hello is not defined
v0 = 5          # Initial velocity 
                    #Invalid syntax, program thinks it is part of the varible definition
                    #Removing =, program infers that it is a variable definition, but does not dare apply this assumption
g = 9.81        # Acceleration of gravity
t = 0.6         # Time

y = v0*t - 0.5*g*t**2       #Verticle postion

print y













