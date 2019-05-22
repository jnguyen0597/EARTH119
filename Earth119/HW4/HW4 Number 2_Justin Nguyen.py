"""
Justin Nguyen
EART 119
Anaconda 2, Python 2.7
Homework 4
"""
import numpy as np
import matplotlib.pyplot as plt
import opt_utils
#=========================================================================
#defining function f(t) - g(t) and derivative function f'(t) - g'(t)

def fct_f(t): # f(t) - g(t)
    return (1.1*(t-2.5)**2) - (5*t + 2.5)

def df_dt(t): # the derivative of the above function
    return 2.2*(t-2.5) - 5
#=========================================================================
#applying newton's method to find crossover points
for t in range(-10,10):
    opt_utils.my_Newton(fct_f, df_dt ,t, tol = 1e-4, N = 20)
    t +=1
#needed time outputs of my_Newton
t_1 = 0.4366
t_2 = 9.1088

#function values for t_1 and t_2
f_t1 = (1.1*(t_1-2.5)**2)
g_t1 = (5*t_1 + 2.5)

f_t2 = (1.1*(t_2-2.5)**2)
g_t2 = (5*t_2 + 2.5)

print f_t1, g_t1, f_t2, g_t2

"""~~~~~~~~~~My Answers~~~~~~~~~~~~
# A) two crossover points in [-10,10]

# B) t1 = ~0.4366, t2= ~9.1088
#    f1(.4366), g1(.4366) = 4.68338, 4.683
#    f2(9.1088), g2(9.1088) = 48.0438, 48.044
"""

"""
C
"""

