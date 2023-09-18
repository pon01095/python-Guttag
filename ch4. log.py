# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 22:26:27 2021

@author: pon01
"""
def find_root_bounds(x, power):
    low = min(-1, x)
    high = max(1, x)
    return low, high


def bisection_solve(x, eval_ans, epsilon, low, high):
  
    ans = (high + low)/2
    while abs(eval_ans(ans) -x) >= epsilon:
        if eval_ans(ans) < x:
            low = ans
        else:
            high = ans
        ans = (high + low) / 2
    return ans
    
    
def find_root(x, power, epsilon):
    if x < 0 and power%2 == 0 :
        return None #음수는 짝수 근이 없다 
    low, high = find_root_bounds(x, power)
    return bisection_solve(x, power, epsilon, low, high) 

def create_eval_ans(i):
    power = i
    return lambda ans: ans**int(power)

def log(x, base, epsilon):
    def find_log_bounds(x, base):
        upper_bound = 0
        while base ** upper_bound < x:
            upper_bound += 1
        return upper_bound - 1, upper_bound
    low, high = find_log_bounds(x, base)
    return bisection_solve(x, lambda ans: base ** ans, epsilon, low, high)


x = int(input('input x: '))
y = int(input('input y: '))
epsilon = float(input('input epsilon: '))

low, high = find_root_bounds(99, 2)
eval_ans = create_eval_ans(y)
print(bisection_solve(x, eval_ans, epsilon, low, high))
print(log(x, y, epsilon))
print(find_root(x, eval_ans, epsilon))

