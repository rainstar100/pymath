# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 19:32:50 2021

@author: Mr Bean
@email: 23122842@qq.com

Decorator->extend the function of the present function such as verification
1)the syntax sugar of the closure function
note: syntax sugar: the logogram (@func) of  func(present func)


"""

def extend_func(func):
    def buildin_extend(*arg,**kwarg):      
        print("I am extending")
        result=func(*arg,**kwarg)
        return result
        
    return buildin_extend


@extend_func
def buy(n):
    print("bought",n)

@extend_func
def sell(a,b):
    print("sold",a,b)
    return (a,b)

