# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np 
np.random.seed(100)
determinant=np.random.randint(1,30,size=(3,3,3))
print(determinant)
det=np.linalg.det(determinant)
print(det)


