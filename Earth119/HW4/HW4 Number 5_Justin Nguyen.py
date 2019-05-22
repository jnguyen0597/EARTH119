# -*- coding: utf-8 -*-
"""
Justin Nguyen
EART 119
Anaconda 2, Python 2.7
Homework 5
"""
import numpy as np
import matplotlib.pyplot as plt

file_in = 'HW4_vertTraj.txt'

t,z = np.genfromtxt(file_in).T

delta_t = t[1::] - t[0:-1]

#Formulas for Velocity and Acceleration
dz_dt = (z[2::] - z[0:-2]) / (2*delta_t[1::])
d2z_dt2 = (z[2::] - 2*z[1:-1] + z[0:-2]) /(delta_t[1::])**2

plt.subplot(311)

ax1 = plt.subplot(311) #Position
ax2 = plt.subplot(312) #Velocity
ax3 = plt.subplot(313) #Acceleration

ax1.plot(t,z)
ax2.plot(t[2::],dz_dt, 'r')
ax3.plot(t[2::],d2z_dt2, 'g')

plt.show()