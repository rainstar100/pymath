# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 10:22:31 2021

nice

@author: Administrator
"""
import numpy as np
import interval

class space():
    
    def __init__(self,space_left,space_right,space_step):
        
        self.left=space_left
        self.right=space_right
        self.step=space_step
        self.range=self.__call__()
    
    def __call__(self):
        
        if self.step==0:
            return interval.Interval(self.left,self.right)
        else:
            return np.arange(self.left,self.right,self.step)
        