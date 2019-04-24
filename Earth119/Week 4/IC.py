# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 08:41:39 2019

@author: jnguy126
"""
import numpy as np
import matplotlib.pyplot as plt
import opt_utils


Plan_Dist = np.genfromtxt( 'planet_distance.txt', usecols= (1,2))
print Plan_Dist
x = Plan_Dist[:, 0]
print 'x', x
y = Plan_Dist[:, 1]    
print 'y', y
#plt.plot( np.log10(x), np.log10(y))
#plt.loglog(x,y)
#plt.plot( x,y,'k-')
#plt.show()

dDic = opt_utils.lin_LS( np.log10( Plan_Dist[0]), np.log10( Plan_Dist[1]))
print dDic
a_yhat = 10**( dDic['a'] ) * Plan_Dist[0]**dDic['b']


plt.figure(1)
plt.subplot( 211)
plt.plot( Plan_Dist[0], Plan_Dist[1], 'ko')
plt.subplot( 212)
plt.loglog( Plan_Dist[0], Plan_Dist[1], 'ko')
plt.loglog( Plan_Dist[0], a_yhat, 'r--')
plt.xlabel( 'Orbital Period')
plt.ylabel( 'Distance')
plt.show()