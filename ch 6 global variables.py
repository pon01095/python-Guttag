# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 14:06:25 2021

@author: LeeHoonGi
"""

def f1():
    global x
    print("x = ", x)
    
def f2():
    global x
    x = 0
    for i in range(10):
        x += 1
        f1()


