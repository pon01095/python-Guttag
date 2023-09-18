# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 13:05:27 2021

@author: LeeHoonGi
"""

def find_root(x, power, epsilon):
    """
    x와 epsilon이 int나 float 이며, int를 power 제곱하며, 
    epsilon > 0 이고 power >= 1이다.
    y**이 x의 epislon 사이에 있는 float y를 리턴한다.
    그러한 float가 없을 때 None을 리턴한다.
    """
    #답이 존재하는 구간 찾기
    if x < 0 and power%2 == 0 :
        return None #음수는 짝수 근이 없다 
    low = min(-1, x)
    high = max(1, x)
    # Use bisection search
    ans = (high + low)/2
    while abs(ans ** power - x) >= epsilon:
        if ans ** power < x:
            low = ans
        else:
            high = ans
        ans = (high + low) / 2
    return ans


def test_find_root(x_vals, powers, epsilons):
    for x in x_vals:
        for p in powers:
            for e in epsilons:
                result = find_root(x, p, e)
                if result == None:
                    val = 'No root exists'
                else:
                    val = 'Okay'
                print(f'x = {x}, power = {p}, epsilon = {e}: {val}')



def is_in(x, y):
    if str(x) in str(y):
        return True
    if str(y) in str(x):
        return True
    else:
        return False
            
    
    


x_vals = (0.25, 8, -8)
powers = (1, 2, 3)
epsilons = (0.1, 0.001, 1)