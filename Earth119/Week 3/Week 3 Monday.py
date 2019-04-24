# -*- coding: utf-8 -*-
"""
Week 3 Data Input/Output - plotting
"""
import numpy as np
import matplotlib.pyplot as plt
#=================================================================================
#  files and variables
#=================================================================================
file_in = 'exoplanet_transit.csv'

r_earth = 6378 # [km]
r_s     = 80*1e3 # [km]
Np      = 3
#=================================================================================
#  load data
#=================================================================================
mData = np.loadtxt( file_in, delimiter = ',', skiprows = 1).T
N     = len( mData[0])
lenPer= int( float(N)/Np) #length period
#Computer difference b/n subsequent samples
aDiff = mData[1][1::] - mData[1][0:-1]
#=================================================================================
#  compute depth of transit
#=================================================================================
aDepth = np.zeros( Np) #array of depth
for i in range( Np):
    #create index vector
    aID = np.arange( lenPer) + lenPer*i
    selMin = aDiff[aID] == aDiff[aID].min()
    selMax = aDiff[aID] == aDiff[aID].max()
    
    iID_min = aID[selMin][0]
    iID_max = aID[selMax][0]

    #compute mean deptth of transit (for each period)
    aDepth[i] = 1 - mData[1, iID_min:iID_max].mean()
    
#Computer size of planet
aR_p = np.sqrt( aDepth)*r_s
print(aR_p)
print( 'size relative to earth', aR_p/r_earth)
#=================================================================================
#  Plotting
#=================================================================================
plt.figure(1)
plt.subplot(211)
plt.plot( mData[0], mData[1], 'ko', ms = 5)
#plt.xlabel( 'Transit Time [hr]')
plt.ylabel( 'Brightness')
plt.show( )

plt.subplot(211)
plt.plot( mData[0][0:-1], aDiff, 'ro', ms = 5)
plt.xlabel( 'Transit Time [hr]')
plt.ylabel( 'Brightness Difference')
plt.show( )

