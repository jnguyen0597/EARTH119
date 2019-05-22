# -*- coding: utf-8 -*-
# python 2.7
"""
"""
import numpy as np
import matplotlib.pyplot as plt
#3D plotting
from mpl_toolkits.mplot3d import axes3d
### my modules
import integrate_utils as int_utils

#================================================
#          fct definition
#================================================
def fct2_xy( x, y):
    return np.sqrt(x**2 + y**2)

def fct_xy( x, y):
    return x*y**2

def fct_gxy( x, y):
    """
    - rectangular domain
     return: -1 for points outside
    """
    f_retVal = -1
    if x >= xmin and x <= xmax and y >= ymin and y <= ymax:
        f_retVal = 1
    return f_retVal

def fct_Fxy_exact( x, y):
    return 0.5*(x**2)*1/.3*( y**3)

#================================================
#           parameters 
#================================================
xmin, xmax = 0, 2
ymin, ymax = 0, 1.5 

a_x = np.linspace( -4, 4, 100)
a_y = np.linspace( -4, 4, 100)

#================================================
#          compute integral 
#================================================
print( 'exact sol: ', round( fct_Fxy_exact(xmax, ymax) - fct_Fxy_exact(xmin, ymin)))

for n in np.arange( 100, 1200, 200):
    #monteCarlo( f_xy, g_xy, xmin, xmax, ymin, ymax, n):
    fInt = int_utils.monteCarlo( fct_xy, fct_gxy, xmin-1, xmax+1, ymin-1, ymax+1, n)
    print( 'no. ran points', n, 'num integral', round(fInt,4), 'exact', 2./3)
#================================================
#            plotting
#================================================
"""
m_X, m_Y = np.meshgrid( a_x, a_y)
m_Z      = fct_xy( m_X, m_Y)
#m_Z      = fct2_xy( m_X, m_Y)
#
fig1 = plt.figure(1, figsize=(10,10))    
ax = axes3d.Axes3D( fig1)
plot1 = ax.plot_surface( m_X, m_Y, m_Z, cmap = plt.cm.coolwarm_r, linewidth=0, shade = True)
cbar = plt.colorbar( plot1, shrink = .5, aspect = 20)
##-----------------labels and legends-------------------------------------
cbar.set_label( 'f(x,y)')
ax.set_xlabel( 'x')
ax.set_ylabel( 'y')
ax.set_zlabel( 'z = f(x,y)')
plt.show()
"""