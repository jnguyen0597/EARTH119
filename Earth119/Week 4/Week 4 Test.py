# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 09:16:08 2019

@author: jnguy126
"""
import numpy as np
import matplotlib.pyplot as plt

import opt_utils


np.random.seed( 12345)


#================================1====================
#           params, dirs, files
#======================================================
xmin, xmax = 0,5
N          = 20
f_a        = 5.0
f_b        = -2.4
f_sigma = 0.5



#================================2====================
#           synthetic data
#======================================================
a_x = np.linspace (xmin, xmax, N)
a_y = f_b * a_x + f_a + np.random.randn( N)*f_sigma





#================================3====================
#           lin LS and plot
#======================================================
dLS = opt_utils.lin_LS( a_x, a_y)
#dLS['a']
plt.figure()
plt.title( str( dLS['R2']))
ax1 = plt.subplot( 111)

# plot data
ax1.plot( a_x, a_y, 'ko', ms=5, mfc = 'none', label = 'Obs.')
# plot model fit
ax1.plot( a_x, dLS['Y_hat'], 'r-', label = 'Model')

ax1.legend(loc = 'upper right')
plt.show()