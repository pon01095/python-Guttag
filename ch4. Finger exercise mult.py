# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 11:22:53 2021

@author: LeeHoonGi
"""

def mult(*arg):
    result = 1
    for i in arg:
        result = result * i
    return result

def mean(*args):
    # 하나 이상의 인수와 모든 인수가 숫자라고 가정
    # 인수들의 중간값
    tot = 0
    for i in args:
        tot += i
    return tot/len(args)

def f(x):
    def g():
        x= 'abc'
        print('x = ', x)
    def h():
        z = x
        print('z = ', z)
    x = x + 1
    print('x = ', x)
    h()
    g()
    print('x = ', x)
    return g
x = 3
z = f(x)
print('x = ', x)
print('z = ', z)
z()
