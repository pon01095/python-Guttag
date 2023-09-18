# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 20:36:27 2021

@author: LeeHoonGi
"""

def fibo_gen(self):
    
    def fibogenerator(n):
        a, b = 1, 1
        for n in range(n):
            yield a
            a, b = b, a + b
    def fibo_for(self):
        x = []
        for i in fibogenerator(self):
            x.append(i)
        return x
    return fibo_for(self)