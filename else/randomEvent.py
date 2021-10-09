# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 17:09:45 2021

@author: Mr Bean
@email: 23122842@qq.com

"""
from randomExperiment import *

class event():
    "eventspace should belong to sampleSpace"
    def __init__(self,randomExperiment,eventSpace):
        
        self.__checked(randomExperiment,eventSpace)
        self.randExp=randomExperiment
        self.eventSpace=eventSpace
        self.frequency=None
        self.probability=self.__probability()
        
        
        
    def __checked(randomExperiment,eventSpace):
        if eventSpace.range not in randomExperiment.sampleSpace.range:
            print("eventspace should be thesubset of sampleSpace")
            raise ValueError
    
    def happened(self,result):
        
        if result in self.eventSpace:
            return True
        else:
            return False
    
    def impossible(self):
        if self.eventSpace.range not in self.randExp.sampleSpace.range:
            return "impossible event"
    
    def inevitable(self):
        if self.eventSpace.range == self.randExp.sampleSpace.range:
            return "inevitble event"
    
    def calFrequency(self,N):
        frequency=0
        for i in self.randExp.Nperform(N):
            if self.happened(i):
                frequency+=1
        self.frequency=frequency/N
        return self.frequency
                
         
    
    def __probability(self):
        pass
    
        
        
        
    