# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 04:20:17 2021

@author: pon01
"""

t1 = (1, 'two', 3)
t2 = (t1, 3.25)
print(t2)
print((t1 + t2))
print((t1 + t2)[3])
print((t1 + t2)[2:4])

def intersect(t1, t2):
    """t1과 t2는 tuple.
    t1과 t2 모두에 포함되는 elements를 포함한 튜플을 리턴"""
    result = ()
    for e in t1:
        if e in t2:
            result += (e,)
    return result
print(intersect((1, 'a', 2), ('b', 2, 'a')))


def find_extreme_divisors(n1, n2):
    """n1과 n2는 양의 정수
     n1과 n2의 1보다 큰 최소공약수와 최대공약수 튜플을 리턴 
     만약 1을 제외한 공약수가 없다면 (None, None)을 리턴"""
    min_val, max_val = None, None
    for i in range(2, min(n1, n2) + 1):
        if n1%i == 0 and n2%i == 0:
            if min_val == None:
                min_val = i
            max_val = i
    return min_val, max_val

#Finger exercise
tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
tupsum = 0
for i in tup:
    tupsum = tupsum + i
tupmean = tupsum / len(tup)

L = ['I did it all', 4, 'love']
for e in L:
    print(e)

L1 = [1, 2, 3]
L2 = L1[-1::-1]
for i in range(len(L1)):
    print(L1[i]*L2[i])
    
L = ['I did it all', 4, 'love']
for e in L:
    print(e)
