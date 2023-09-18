# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 12:41:18 2021

@author: pon01
"""
import copy 

Techs = ['MIT', 'Caltech'] 
Ivys = ['Harvard', 'Yale', 'Brown']
Univs = [Techs, Ivys]
Univs1 = [['MIT', 'Caltech'] , ['Harvard', 'Yale', 'Brown']]


print('Univs =', Univs)
print('Univs1 =', Univs1)
print(Univs == Univs1)
print(id(Univs) == id(Univs1)) #test object equality

Techs.append('RPI')

print(Univs == Univs1) #test value equality
print(id(Univs) == id(Univs1)) #test object equality
print(Univs is Univs1) #test object equality
print('Id of Univs =', id(Univs))
print('Id of Univs1 =', id(Univs1))


def remove_dups(L1, L2):
    """L1과 L2는 리스트
 L1에 있으면서 L2에 동시에 존재하는 모든 L1의 원소를 제거"""
    for e1 in L1[:]:
        print('L1 = ', L1)
        print('e1 = ', e1)
        if e1 in L2:
            L1.remove(e1)
L1 = [1,2,3,4]
L2 = [1,2,5,6]
remove_dups(L1, L2)
print('L1 =', L1)


L = [2]
L1 = L
L2 = L1[:]
L3 = copy.deepcopy(L1)
print(f'L ={L}, L1 = {L1}, L2 = {L2}, L3 = {L3}')
L.append(3)
print(f'L ={L}, L1 = {L1}, L2 = {L2}, L3 = {L3}')


L = [2]
L1 = [L]
L2 = L1[:]
L3 = copy.deepcopy(L1)
print(f'L ={L}, L1 = {L1}, L2 = {L2}, L3 = {L3}')
L.append(3)
print(f'L ={L}, L1 = {L1}, L2 = {L2}, L3 = {L3}')

L = [x**2 for x in range(1,7)]
print(L)
L = [(x, y)
 for x in range(6) if x%2 == 0
 for y in range(6) if y%3 == 0]

L = []
for x in range(6):
    if x%2 == 0:
        for y in range(6):
            if y%3 == 0:
                L.append((x, y))
                
                
def gen_primes(to):
 
    primes = []
    for x in range(2, to):
        is_prime = True
        for y in range(3, x):
            if x%y == 0:
                is_prime = False
        if is_prime:
            primes.append(x)
    return primes