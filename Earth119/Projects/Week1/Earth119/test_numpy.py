# -*- coding: utf-8 -*-
"""
script that test numpy functionality

"""
#Interpreter used: Python 2.7
import numpy as np

N = 10 #number of elements in vector
start = 1
stop = 10 #stopping value of vector -1
step = 1


aV = np.arange(start, stop, step)
print (aV)

aV2 = np.linspace( start, stop, N)
print (aV2)





