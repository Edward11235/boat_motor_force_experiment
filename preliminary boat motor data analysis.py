# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 23:28:30 2024

@author: 24929
"""

import numpy as np
from matplotlib import pylab as plt
from scipy.optimize import curve_fit
from scipy import constants as cst

begin_V = 11.4
end_V = 11.1



para, meas1, meas2, meas3 = np.loadtxt('baby boat.txt', skiprows=1, delimiter=',', unpack=True)
meas = (meas1 + meas2 + meas3) / 3
meas*= 9.8


plt.figure()
plt.plot(para, meas, label='data')
plt.xlabel('Boat Motor Parameter')
plt.ylabel('Force (N)')
plt.legend()