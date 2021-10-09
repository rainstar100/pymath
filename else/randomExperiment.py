# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 21:52:45 2021

@author: Administrator
"""
from abc import ABC,abstractmethod
import numpy as np
from space import space

class randomExperiment(ABC): 
    
    def __init__(self,space):
        self.sampleSpace=space
          
    @abstractmethod
    def Nperform(self,N): 
        "Note the return should be confirmed with sampleSpace.\
        for example : \
        the space is countinue,please design countinue experiment results; \
        the space is discrete ,please design discrete  experiment reslults"
        pass
        return 
    


        

