# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 14:28:30 2021

@author: LeeHoonGi
"""

def printName(firstName, lastName, reverse= False):
    if reverse:
        print(lastName + ", " + firstName)
    else:
        print(firstName, lastName)
        
printName("John", "Doe", False)
printName("John", lastName="Doe", reverse=False)
printName(lastName="Doe", reverse=False, firstName="John")

printName("John", "Doe")
