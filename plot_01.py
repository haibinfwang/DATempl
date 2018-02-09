#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
plot_01.py
Example code for plottin with matplotlib


Created on Fri Feb  9 12:21:18 2018
@author: wang
"""
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
%matplotlib qt5

#%% 1. Plot with OO api
plt.figure(1)
plt.clf()
ax=plt.subplot()
ax.plot(np.arange(10),np.arange(10),'-',color='b')


#%% Change background color


