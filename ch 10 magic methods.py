# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 16:13:58 2021

@author: LeeHoonGi"""

class Toy(object):
    def __init__(self):
        self._elems = []  # 빈 list 생성
    def add(self, new_elems):
        """new_elems is a list""" 
        self._elems += new_elems 
    def __len__(self):
        return len(self._elems)
    def __add__(self, other):
        new_toy = Toy()
        new_toy._elems = self._elems + other._elems
        return new_toy
    def __eq__(self, other):
        return self._elems == other._elems
    def __str__(self):
        return str(self._elems)
    def __hash__(self):
        return id(self)


      
t1 = Toy()
t2 = Toy()
t1.add(['a', 'b'])
t2.add([3, 4])
t3 = t1 + t2
print('The value of t3 is', t3)
print('The length of t3 is', len(t3))
d = {t1: 'A', t2 : 'B'}
print('The value', d[t1], ' is associated with the key t1 in d.')