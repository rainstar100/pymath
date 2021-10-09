# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 16:46:39 2021

@author: Administrator
"""

from randomExperiment import *

class tossCoin(randomExperiment):
      
    def Nperform(self,N=100): 
        
        results=np.random.randint(self.sampleSpace.left,self.sampleSpace.right,N)
        
        return results
    
        
        
test=tossCoin(space(1,4,1))
