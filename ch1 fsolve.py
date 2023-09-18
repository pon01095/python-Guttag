# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 23:16:58 2021

@author: pon01
"""

from scipy.optimize import fsolve
import math


x = 25
print(math.sqrt(25))	

def func(ans):
    return ans**2 - x

x0 = fsolve(func, 0.3)		# 비선형방정식 solver
print(x0)
