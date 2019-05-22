#!/bin/python2.7
"""

    1) plot direction field for a simple first order ODE
    2) compute numerical appox using Forward Euler
    3) compare to analytical solution

- example is concentration balance of salt in a volume, V from Brannan & Boyce, Differential Equations

"""
from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
#--------------my modules----------------------------
#import ODE.ode_utils as utils
def fct_conc(t, c_in, m0, Q, V):
    """
    - analytical solution to: m' = c_in*Q - Q/V*m
    :param t:    - time
    :param c_in: - salt concentration
    :param m0:   - IC
    :param Q:    - flow rate
    :param V:    - volume
    :return: - analytical solution as fct(t, m0)
    """
    return c_in*V + (m0 - c_in*V)*np.exp( -Q/V * t)

def directionField(ax, a_t, a_y, params, **kwargs):
    """

    :param at:  - time vector
    :param a_y: - dependent variable vector

    :kwargs scale_fac - for vector length
                        default - 40
            width     - width of the vector, default = 1e-3
    """
    scale_fac = 40
    width     = 1e-3
    if 'scale_fac' in kwargs.keys() and kwargs['scale_fac'] is not None:
        scale_fac = kwargs['scale_fac']
    if 'width' in kwargs.keys() and kwargs['width'] is not None:
        width = kwargs['width']
    #create t - m mesh
    m_t, m_y   = np.meshgrid( a_t, a_y)
    # note that you could use a key word argument to switch between different types of ODEs
    m_YY_prime = y_prime_p_g( m_y, params)

    ###plot: use plot quiver: https://matplotlib.org/api/_as_gen/matplotlib.pyplot.quiver.html
    # quiver takes coordinate of starting point and end of point of vector, use matrix of ones for x-component of vector
    ax.quiver( m_t, m_y, np.ones((m_t[0].shape[0], m_t.shape[0]))*.5, m_YY_prime, scale = scale_fac, width = width, headwidth=1e-6)

def y_prime_p_g( yn, params):
    """
    - direction field vectors (y') at every t and y

    only for simple ODEs of the form:
    y' + p(t)y = g(t)
    :return: y' = -p(t)y + g(t)
    """
    return params[0] - params[1]*yn
#------------------------------------------------------------------------
#                   params, files, dir
#------------------------------------------------------------------------
## time range and step
h    = 1 # in seconds
tmin = 0
tmax = 100
a_t  = np.arange( tmin, tmax+h, h)
nSteps = len( a_t)
###
c_in = .25 #[kg/m^3], salt concentration in
V    = 100. # m3,  total volume of tank
Q    = 3. #m3/s, flow rate
# initial conditions
f_m0 = 35
#--------------------------1---------------------------------------------
#                     direction field
#------------------------------------------------------------------------
# specify parameters for: y' = -py + g, p and g are constants
p = Q/V
g = c_in*Q
# specify possible solution vector for geometric solution
a_y_sim = np.arange( 0, 50, 1)
#--------------------------3---------------------------------------------
#                compute numerical, and ana solutions
#------------------------------------------------------------------------
# plt.figure(1, figsize=(8,8))
# ax = plt.axes( [.12, .12,.83,.83])
# for f_m0 in np.arange( 0, 51, 5):
# :TODO analytical solution
a_m_ana = fct_conc(a_t, c_in, f_m0, Q, V)
# numerical solution for n time steps
a_m_num    = np.zeros( nSteps)
#:TODO set initial condition
a_m_num[0] = f_m0
for i in range( nSteps-1):
    # slope at previous time step, i, fn = y'( yn)
    fn          = y_prime_p_g( a_m_num[i], np.array([g, p]))
    #:TODO  euler formula: y[n+1] = y[n] + fn*h
    a_m_num[i+1] = a_m_num[i] + fn*h
#--------------------------4---------------------------------------------
#                       plots
#------------------------------------------------------------------------
plt.figure(1, figsize=(8,8))
ax = plt.axes( [.12, .12,.83,.83])
## use ode_utils to plot direction field
directionField(ax, a_t, a_y_sim, [g,p], width = None, scale_fac = None)
# plot numerical and analytical solution
ax.plot( a_t, a_m_num, 'ko', mfc = 'none', ms = 5, label = 'num. sol.')
ax.plot( a_t, a_m_ana, 'r-', lw = 1, label = 'exact')
ax.legend( loc = 'lower right')

##legend and labels
ax.set_xlabel( 'Time [s]')
ax.set_ylabel( 'Salt Mass [kg]')
plt.show()

