# -*- coding: utf-8 -*-
"""
animation of global earthquake 
locations from 2000 to 2019
- plotted annually
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap as Basemap
#=================================================================================
#  file and parameters
#=================================================================================
file_eq = 'globalEqs.txt'








#=================================================================================
#  load data
#=================================================================================
aYr     = np.genfromtxt( file_eq, skip_header = 1,
                        usecols=(0), delimiter = '-',
                        dtype = int )
print( np.unique( aYr))
mLoc = np.genfromtxt( file_eq, skip_header = 1,
                     delimiter = '-', usecols=(2,1),
                     dtype = float).T









#=================================================================================
#  plot eq map using basemap
#=================================================================================
for it in np.unique( aYr):
    sel_eq = it == aYr
    print( 'no of eqs. in %i: %i'%(it, sel_eq.sum()))
    plt.figure()
    plt.title( str(it))


    m = Basemap( )
    m.drawcoastlines()
    
    
    a_X, a_Y  = m( mLoc[0][sel_eq], mLoc[1][sel_eq]) 
    
    #plt.plot( a_X, a_Y, 'ro', ms = 5, mew = 1.5, mfc = 'none')
    plt.scatter( a_X, a_Y, c = mLoc[2][sel_eq],
                s = np.exp( mLoc[2][sel_eq]-3),)
    cbar = plt.colorbar( plot1, orientation = 'horizontal')
    cbar.set_labael( 'Magnitude')
    plt.pause( 1.5)
    plt. clf()





#=================================================================================
#  load data
#=================================================================================

