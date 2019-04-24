# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 19:42:53 2019

@author: jnguy126
"""

import numpy as np

total = 0
n = 10

for i in range(n+1):
    term = 8*((4*i+1)*(4*i+3))**-1
    total = total + term
    
    print ('term:' + str(term))

print (total)





