#!/bin/python2.7
"""

solve second order, homogeneous ODE: damped, harmonic oscillator

- compare analytical and numerical (both Euler and Range Kutta)

ODE: my''(t) + ky(t) = 0
        f(t) = F*cos(wt)
        w0**2 = k/m


"""
from __future__ import division

import os
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

#--------------fct definitions--------------------------
def runge_kutta_vec( tn, Yn, h, params):
    """
    fourth order runge kutta stepper, for single or system of  ODEs
    :input       tn           - current time step
                 Yn           - function value at time tn
                 fct_RHS      - vectorised function that defines slope (derivative) at point (t, y)
                                = all RHS of the system of ODEs

                 params   - py dictionary that includes step size 'h'
                            and all parameters needed in function:
                            fct_RHS

    :return: a_fn1 - values of derivatives at current tn for all ODEs
    """
    h = params['h']
    Kn1 = (fct_RHS( tn, Yn, params))
    Kn2 = (fct_RHS( tn + (h/2.), Yn + (Kn1)/2., params))
    Kn3 = (fct_RHS( tn + (h/2.), Yn + (Kn2)/2.,   params))
    Kn4 = (fct_RHS( tn + h, Yn + Kn3, params))
    return (Kn1 + 2*Kn2 + 2*Kn3 + Kn4)/6.

def oscillator( t, Yn, par):
    """
    - describe second order ODE for forced, undamped oscillation by two first order ODEs
        ODE:  y''(t) + w0**2y(t) = f(t)
                                f(t) = F*cos(w*t)
             u   =  y; v = y'
             u'  =  v
             v'  = -k*u + f(t)
    :input - t - time vector
             u  - displacement
             v  - velocity
             F  - amplitude of forcing fct
             w0 -  parameter: natural fequency: w0**2 = k/m

    :return:  [displ, vel]
    """
    u, v = Yn[0], Yn[1]
    fn1 = v
    fn2 = -par['w0']**2*u - par['gamma']*v
    return np.array([fn1, fn2])

def num_sol( at, y0, par):
    """
    - solve second order ODE for forced, undamped oscillation by solving two first order ODEs
       ODE:  y''(t) + ky(t) = f(t)
                              f(t) = F*cos(w*t)
    :param y0:         - IC
    :param at  :       - time vector
    :param par :       - dictionary with fct parameters
    :return: ay_hat    - forward Euler
             ay_hat_rk = 4th order runge kutta
    """
    nSteps    = at.shape[0]
    # create vectors for displacement and velocity
    au_hat    = np.zeros( nSteps)
    av_hat    = np.zeros( at.shape[0])
    # set initial conditions
    au_hat[0] = y0[0]
    av_hat[0] = y0[1]
    for i in range( nSteps-1):
        # slope at previous time step, i
        fn1, fn2     = runge_kutta_vec( at[i], np.array([au_hat[i], av_hat[i]]), oscillator, dPar)
        # forward Euler: y[n+1] = y[n] + fn*h
        #fn1 = av_hat[i]
        #fn2 = -par['w0']**2*au_hat[i]

        # Integration step: Runge Kutta or Euler formula
        au_hat[i+1] = au_hat[i] + fn1*par['h']
        av_hat[i+1] = av_hat[i] + fn2*par['h']
    return au_hat, av_hat

#-------------------------------1----------------------------------------
#                   params, files, dir
#------------------------------------------------------------------------
dPar = { #frequencies
        'w0'    :  .8, #= sqrt(k/m) --> natural frequency
        'gamma' :   0, # damping constant, set to 0 to compare to exact solution
        # initial conditions for displ. and velocity
        'y01' : 0, 'y02' : 0,
        # time stepping
        'h'      : 1e-2,
        'tStart' : 0,
        'tStop'  : 20*np.pi,}

#--------------------------------2---------------------------------------
#                      analytical solution
#------------------------------------------------------------------------
a_t = np.arange( dPar['tStart'], dPar['tStop']+dPar['h'], dPar['h'])
ay_ana    = dPar['y01']*np.cos( dPar['w0']*a_t)
#--------------------------------3---------------------------------------
#                      numerical solutions
#------------------------------------------------------------------------
aU_num, aV_num = num_sol(  a_t, [dPar['y01'], dPar['y02']], dPar)
#--------------------------------4---------------------------------------
#                            plots
#------------------------------------------------------------------------
plt.figure(1)
ax = plt.subplot( 111) #plt.axes( [.12, .12, .83, .83])
ax.plot( a_t,   aU_num,   'k-', lw = 3, alpha = .3, label = 'num - displ.')
ax.plot( a_t,  ay_ana, 'r--', lw = 1, label = 'ana')
ax.set_xlabel( 'Time [s]')
ax.set_ylabel( 'Displacement [mm]')
ax.legend( loc = 'upper left')
plt.show()