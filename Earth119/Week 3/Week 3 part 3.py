# -*- coding: utf-8 -*-
"""
Compute temportal earthquake rate change
for KTB fluid injection experiment
"""
import numpy as np
import matplotlib.pyplot as plt

#=================================================================================
#  load data
#=================================================================================
def comp_rate( a_t, k):
    """
    - compute rate change for time vector a_t
    :input
            a_t - time vector
            k   - sample window - control smoothness
            
    :output  a_bin, a_rate
    """
    aS = np.arange( 0, a_t.shape[0], 1)
    a_bin = np.zeros( aS.shape[0])
    a_rate= np.zeros( aS.shape[0])
    iS = 0
    for s_step in aS:
        i1, i2      = s_step, s_step+k
        a_rate[i]   = k/( a_t[i2] - a_t[i1])
        a_bin       = 0.5*( a_t[i1] + a_t[i2])
        iS += 1
    return a_bin, a_rate

#=================================================================================
#  load data
#=================================================================================
file_inj = 'KTB_inject.txt'
file_eq  = 'KTB_mag.txt'

#sample
k_win = 10


t0      = float() #starting time forp lotting
aT_eq   = np.array([]) # timing of the eathquakes
aMag    = np.array([])

aT_inj  = np.array([])
aV      = np.array([])

#=================================================================================
#  load data
#=================================================================================
mData = np.loadtxt( file_eq).T
aT_eq   = np.array([0])
aMag    = np.array([1])

mData = np.loadtxt( file_inj).T
aT_inj  = np.array([3])
aV      = np.array([4])

sel = aV > 0
aV = aV[sel]
aT_inj = aT_inj[sel]

t0      = aT_inj[0]
aT_inj -= t0
aT_eq -= t0
aT_inj = aT_inj/300
aT_eq = aT_eq/300

a_tbin, a_rate = comp_rate( aT_eq, k_win)


#=================================================================================
#  Plot
#=================================================================================
plt.figure(1)
ax1 = plt.subplot(211)
ax1.plot( aT_eq, aMag, 'b-')
ax1
ax2 = plt.subplot(212)
ax2.plt( aT_inj, aV, 'ko')
ax2.set_xlim( ax1.get_xlim())
plt.show()








