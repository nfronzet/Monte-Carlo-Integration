# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 14:08:41 2018

@author: Nicola
"""

import numpy as np
import scipy.integrate as integrate
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import random as rand
import time as tm

#integrand function
def integrand(t):
    return np.cos(t)

def integrand3d(x, y):
    return x**2 + y**2

#compute min and max of function f between t1 and t2
def functionOptimize(f, t1, t2):
    dt = 0.0001
    fMin = 0.0
    fMax = 0.0
    t = t1
    while (t <= t2):
        val = f(t)
        if (val < fMin):
            fMin = val
        if (val > fMax):
            fMax = val
        t += dt
    return fMin, fMax

#compute min and max of 3d function f between (x1,x2) and (y1,y2)
def functionOptimize3d(f, x1, x2, y1, y2):
    ds = 0.01
    fMin = 0.0
    fMax = 0.0
    x = x1
    while (x <= x2):
        y = y1
        while (y <= y2):
            val = f(x,y)
            if (val < fMin):
                fMin = val
            if (val > fMax):
                fMax = val
            y += ds
        x += ds
    return fMin, fMax

#Monte Carlo integration of function f between t1 an t2.
#nTrials: number of trials. PPT: number of points used per trial
def MCIntegrate(f, nTrials, PPT, t1, t2):
    #initialize lower bound, upper bound and final result
    lBound, uBound = functionOptimize(f,t1,t2)
    result = 0.0
    for i in range(0, nTrials):
        tot = 0
        #number of "hits" above the line y=0, gives positive portion of area
        phits = 0
        #number of "hits" below the line y=0, gives negative portion of area
        nhits = 0
        for j in range (0, PPT):
            k = rand.uniform(t1,t2)
            y = rand.uniform(lBound,uBound)
            tot = tot + 1
            val = f(k)
            if (val >= 0 and y >= 0 and y <= val):
                phits = phits + 1
                plt.plot(k,y,'r.-')
            elif (val < 0 and y >= val and y <= 0):
                nhits = nhits + 1
                plt.plot(k,y,'r.-') 
        result = result + (phits/tot)*(t2-t1)*(uBound-lBound) - (nhits/tot)*(t2-t1)*(uBound-lBound)
    #return value is the average of all computations 
    return result/nTrials

#Monte Carlo integration of 3d function f between (x1,x2) and (y1,y2)
#nTrials: number of trials. PPT: number of points used per trial
def MCIntegrate3d(f, nTrials, PPT, x1, x2, y1, y2):
    #initialize lower bound, upper bound and final result
    lBound, uBound = functionOptimize3d(f,x1,x2,y1,y2)
    result = 0.0
    for i in range(0, nTrials):
        tot = 0
        #number of "hits" above the plane z=0, gives positive portion of volume
        phits = 0
        #number of "hits" below the plane z=0, gives negative portion of volume
        nhits = 0
        
        for j in range (0, PPT):
            rx = rand.uniform(x1,x2)
            vx = np.ravel(rx)
            ry = rand.uniform(y1,y2)
            vy = np.ravel(ry)
            rz = rand.uniform(lBound,uBound)
            vz = np.ravel(rz)
            tot = tot + 1
            val = f(rx,ry)
            if (val >= 0 and rz >= 0 and rz <= val):
                phits = phits + 1
                ax.scatter(vx, vy, vz, c=vz, cmap='viridis', linewidth=0.5);
            elif (val < 0 and rz >= val and rz <= 0):
                nhits = nhits + 1
                ax.scatter(vx, vy, vz, c=vz, cmap='viridis', linewidth=0.5);
        result = result + (phits/tot)*(x2-x1)*(y2-y1)*(uBound-lBound) - (nhits/tot)*(x2-x1)*(y2-y1)*(uBound-lBound)
    #return value is the average of all computations 
    return result/nTrials
'''
t = np.linspace(0,6)
x = integrand(t)
plt.plot(t,x)
I = integrate.quad(integrand,0,(3/2)*np.pi)
initTime = tm.time()
I_MC = MCIntegrate(integrand,5,1000,0,(3/2)*np.pi)
print('MC result: ' + str(I_MC))
print ('Expected result: ' + str(I))
print('Computation completed in ' + str.format('{0:.4f}', tm.time()-initTime) + 's')
'''

x = np.linspace(-1, 3)
y = np.linspace(-1, 3)

X, Y = np.meshgrid(x, y)
Z = integrand3d(X, Y)

ax = plt.axes(projection='3d')
ax.plot_wireframe(X, Y, Z, color='black')
ax.view_init(60, 35)

I = integrate.dblquad(integrand3d,0,2,0,2)

initTime = tm.time()

I_MC3 = MCIntegrate3d(integrand3d,5,1000,0,2,0,2)
print('MC result: ' + str(I_MC3))
print ('Expected result: ' + str(I))
print('Computation completed in ' + str.format('{0:.4f}', tm.time()-initTime) + 's')

