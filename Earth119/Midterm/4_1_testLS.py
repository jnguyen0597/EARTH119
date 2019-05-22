'''
Created on April 15th, 2019


    - test linear least squares fits to point clouds with different aspect ratios
        (1) y = bx + c + err(f_sigma)   (err - normal error)

@author: tgoebel
'''

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats
np.random.seed( 123456)
#===================================================================================
#                           function def
#===================================================================================
import opt_utils as utils

#===================================================================================
#                           files, parameters
#===================================================================================
# interval over which linear fct is evaluated
xmin,xmax = 0, 5
# parameters
N    = 200
f_a  = 5.
f_b  = -2.4
f_sigma = .5 # change to 5 then to 10

#===================================================================================
#                          synthetic data
#===================================================================================
a_x = np.linspace( xmin, xmax, N)
a_y = f_b*a_x + f_a + np.random.randn( N)*f_sigma

#===================================================================================
#                           data fits
#===================================================================================
dLS = utils.lin_LS( a_x, a_y)
for tag, item in dLS.items():
    if isinstance( item, (int, float)):
        print( tag, item)
print( dLS['R2'], dLS['r_p']**2)
## same result with scipy
slope, intercept, r_p, prob, stderr = scipy.stats.linregress( a_x, a_y)
print('scipy', slope, intercept, r_p)

#===================================================================================
#                              plots
#===================================================================================
plt.figure(1)
ax1 = plt.subplot(111)
ax1.plot( a_x, a_y, 'ko', ms = 5, mew = 1, mfc = 'none')
ax1.plot( a_x, dLS['Y_hat'], 'r--', label = 'y = %.1f x + %.1f, R2=%.2f'%( dLS['b'], dLS['a'], dLS['R2']))
# ax1.hexbin( a_x, a_y, cmap = plt.cm.Blues)
ax1.legend( loc = 'upper right')
plt.show()