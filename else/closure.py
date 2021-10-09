# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 15:27:19 2021

closure:
    1)the return of function is the reference of its buildin function.
    2)their params are independent each other
f(*arg,**kwarg):
    g(*arg,**kwarg):
        pass
    return g
g--> extend the operation of H ,meanwhile return the reference of H
f--> return the reference of G

    

@author: Mr Bean
@email: 23122842@qq.com

"""
# closure without params
def print_closure():
    
    def buildin_its():
        print("I am buildin Func")
    
    return buildin_its

#closure with params
def number_closure(a):
    def build_its():
        #a=3 loacal->enviorment of buildin
        print("the return is",a)
    return build_its

def str_closure(a,b):
    def buildin_its(*arg,**kwarg):
        print(a)
        print(b)
        print(arg)
        print(kwarg)
        
    return buildin_its
        

def cover_closure(a,b):
    def buildin_its(a,b):
        print(a)
        print(b)


        
    return buildin_its

  