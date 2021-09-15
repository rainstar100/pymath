# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 20:48:54 2021

@author: Administrator
"""

import numpy as np
import matplotlib.pyplot as plt


x=np.linspace(-np.pi,np.pi,num=1000)
y=np.sin(x)

plt.plot(x,y)

plt.show()