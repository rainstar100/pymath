# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 14:34:51 2010

@author: Administrator
"""

import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-10,10,num=1000)
y=abs(x)

plt.plot(x,y)
