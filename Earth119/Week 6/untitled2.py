# -*- coding: utf-8 -*-
"""
Created on Mon May  6 09:24:38 2019

@author: jnguy126
"""
import numpy as np
import matplotlib.pyplot as plt
####
# fct def
####
def fct_xy( x, y):
    return x*y**2

def fct_gxy( x, y):
    """
    - retangular domain
    return: -1 for points outside (retVal)
    
    """
    f_retVal = -1
    if x >= xmin and x >= xmax and y >= ymin and y >= ymax:
        f_retVal = 1
    return 



#####
#Param
#####



#####
#computation
#####

