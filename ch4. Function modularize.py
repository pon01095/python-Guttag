# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 22:26:27 2021

@author: pon01
"""
def find_root_bounds(x, power):
    """x는 float, 양의 정수 int 만큼 제곱한다
    low** power <= x이며 high ** power >= x인low, high를 리턴한다. 
    """
    low = min(-1, x)
    high = max(1, x)
    return low, high

def bisection_solve(x, power, epsilon, low, high):
    """x, epsilon, low, high는 float이다.
    epsilon > 0
    low <= high 이며 low와 high 사이에 ans가 있다.
    ans ** power는 x의 epislon 범위에 있다.
    ans s.t를 리턴하고 ans ** power는 x의 epsilon 범위에 있다."""
    ans = (high + low)/2
    while abs(ans**power -x) >= epsilon:
        if ans**power < x:
            low = ans
        else:
            high = ans
        ans = (high + low) / 2
    return ans
    
    
def find_root(x, power, epsilon):
    """
    x와 epsilon이 int나 float 이며, int를 power 제곱하며, 
    epsilon > 0 이고 power >= 1이다.
    y**이 x의 epislon 범위에 있는 float y를 리턴한다.
    그러한 float가 없을 때 None을 리턴한다.
    """
    if x < 0 and power%2 == 0 :
        return None #음수는 짝수 근이 없다 
    low, high = find_root_bounds(x, power)
    return bisection_solve(x, power, epsilon, low, high) 
