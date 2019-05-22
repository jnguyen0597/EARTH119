#! python2.7
"""
Solve 1D-Heat equation for 1D rod with length l
       or infinite wall with thickness l,
       with different boundary temperature outside the domain

       du/dt    = alpha*d^2u/dx^2 + g(x,t)
   here: g(x,t) =  0
         alpha  = thermal diffusivity

--> units of t, x, and alpha have to be in agreement
a) solve the PDE and set BC
b) plot steady state at t-> inf. u_t = u_xx = 0
    u(x) = c1 x + c2; Fixed BC: u(x) = (B-A)/L x + A, A - left BC, B = right BC
c) test numerical stability: stable for dt <= dx**2/(2*alpha)
"""
from __future__ import division

import numpy as np
import matplotlib.pyplot as plt
#=====================================================================
#                   params
#=====================================================================
f_Alpha = 5*10**(-7) #m2/s brick see https://en.wikipedia.org/wiki/Thermal_diffusivity
f_L     = 0.1 # length of rod [m]
#-----------initial and BC------------
f_Uin   = 40 # in degree C, left boundary
f_Uout  = 20 # in degree C, right boundary
# constant initial temp
f_U0      = 0
#-------spatial discretization--------
i_Nx      = 100 # number of nodes in x
f_dx      = f_L/(i_Nx-1) # node spacing
#----time -discretization-------------
f_dt      = 1 # time step in 
f_tmax    = 10*3600 #*60  # in seconds

#------plotting
plot_step = 40 #plot every nth step
#=========================1===========================================
#              space/time discretization and IC
#=====================================================================
a_x    = np.linspace( 0, f_L, i_Nx)
a_t    = np.arange( 0, f_tmax+f_dt, f_dt)
i_Nt   = len( a_t) #int( round( f_tmax/f_dt))+1 # n nodes in t
print('space', i_Nx, len( a_x), a_x[1]-a_x[0],    f_dx)
print('time',  i_Nt, len( a_t), a_t[1]-a_t[0], f_dt)

# IC: aU0 = const ( = 0)
aU     = np.ones( i_Nx)*f_U0
print( 'number of time steps', i_Nt, 'tmax in days: ', f_tmax/(24*3600))
print( 'delta t: ', f_dt, 'in [s],   stability lim for delta t: ', f_dx**2/(2*f_Alpha))

#TODO: write down  steady-state solution
#a_x_ss = np.linspace( 0, f_L, 3)
#aU_ss = ????
#=============================2=======================================
#                     solve 1d-heat
#=====================================================================
# initialize time derivative vector
a_dUdt   = np.zeros( len( a_x))

#plt.figure(1)
fig, ax1 = plt.subplots( )
for n in range( len(a_t)):# loop over time increments

    for i in range( 1, i_Nx-1): #spatial loop without boundary nodes
        # TODO: central difference solution
        a_dUdt[i] = f_Alpha*( (aU[i+1]-2*aU[i] +aU[i-1])/ f_dx**2)
    # vectorized central difference
    # TODO: replace for loop with vectorized solution from HW4
    # ?????????
    # set boundary conditions
    aU[0] = f_Uin # Left BC
    aU[-1]= f_Uout # Right BC
    # TODO: forward Euler Formula to get u(x,t)
    #aU_new = aU + dt* a_dUdt
    #aU  = aU_new
    aU  = aU + f_dt* a_dUdt
    #=========================3===========================================
    #               plot temp. u(x) for every mth time step
    #=====================================================================
    print( 'time step: ', round( a_t[n]/3600,3), 'h')#,(n+1)/plot_step,(n+1)%plot_step
    if (n+1)%plot_step == 0:
        ax1.cla()
        ax1.set_title( 'Time Step: %.2f [h]'%( a_t[n]/3600))
        ax1.plot( a_x, aU,  'ko', ms = 4, mew = 1, mfc = 'none', label = 'u(x,t)')
        # plot wall boundaries
        ax1.plot( [0,0],   [0, max( f_Uin, f_Uout)], 'r--')
        ax1.plot( [f_L,f_L], [0, max( f_Uin, f_Uout)], 'r--')
        # plot steady-state solution
        #ax1.plot( a_x_ss, aU_ss, 'b--', label = 'u-ss')

        #ax1.plot( a_x, aU_ana, 'r-')
        #-----------------limits and labels-------------------------------------
        ax1.set_xlabel( 'Distance [m]')
        ax1.set_ylabel( 'Temperature [degree C]')
        ax1.legend( loc = 'lower left')
        ax1.set_xlim( -.1*f_L, 1.1*f_L)
        ax1.set_ylim( 0, max( f_Uin, f_Uout))
        plt.pause( 0.01)

#plt.show()







