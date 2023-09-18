# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 16:50:24 2021

@author: pon01
"""

def apply_to_each(L, f):
    """
    Parameters
    ----------
    L : TYPE
        List.
    f : TYPE
        function.

    Returns
    -------
    L의 각 요소 e를 f(e)로 대체하여 L을 변경합니다.
    """
    for i in range(len(L)):
        L[i] = f(L[i])
        
        
L = [1, -2, 3.33]
print('L = ', L)
print('Apply abs to each element of  L')
apply_to_each(L, abs)    
print('L = ', L)
print('Apply int to each element of  L')
apply_to_each(L, int)    
print('L = ', L)
print('Apply squaring to each element of  L')
apply_to_each(L, lambda x: x**2)    
print('L = ', L)

list(map(str, range(10))) 


for i in map(lambda x: x**2, [2, 6, 4]):
    print(i)
    
    
L1 = [1, 28, 36]
L2 = [2, 57, 9]
for i in map(min, L1, L2):
    print(i)
    
#Finger exercise
def f(L1, L2):
    """L1, L2 lists of same length of numbers
    returns the sum of raising each element in L1
    to the power of the element at the same index in L2
    For example, f([1,2], [2,3]) returns 9"""
    L3 = []
    ret = []  
    for i in range(len(L1[:])):
        L3.append(L1[i]**L2[i])
    ret = sum(L3)
            
    return ret

s = "abc def ghi jkl"
s.split(" ")
