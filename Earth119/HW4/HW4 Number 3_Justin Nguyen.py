# -*- coding: utf-8 -*-
"""
Justin Nguyen
EART 119
Anaconda 2, Python 2.7
Homework 3
"""
def my_Newton( fct, df_dt, x0, tol = 1e-6, N = 20):
    """
    :param fct:     - find root of this fct. closes to x0
    :param dfct_dt: - derivatice of fct
    :param x0:      - initial guess of solution
    :param N:       - number of iterations, default = 20
    :param tol:     - tolerance, default = 1e-4
    :return: f_r0 - closest to x0
    """
    xn = float( x0)
    i  = 0
    while abs( fct( xn)) > tol and i < N: # could also set fct. to ~0 to find root instead of min.
        x_next = xn - fct( xn)/df_dt( xn)
        print i, abs( fct( xn)), x_next
        xn = float( x_next)
        i += 1
        if abs(fct(xn**(i+1)) - fct(xn**i))>tol: #stop iterations at set conditions
            break
        
    if abs( fct( xn)) > tol:# no solution found
        return None
    else:
        return float( x_next)