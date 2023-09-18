# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 20:36:53 2021

@author: LeeHoonGi
"""
import fib as fib


name_handle = open('kids.txt', 'w')

  
name_handle.write(str(fib.fibo_gen(10)))
name_handle.writeliness('피보나치')
# data = name_handle.read()
# print(data)
name_handle.close()


with open('kids.txt', 'r') as name_handle:
    for line in name_handle:
        print(line)
