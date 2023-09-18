# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 23:04:49 2021

@author: pon01
"""
def harmonic_sum(n):
    x = []
    for i in range(n):
        if i == 0:
            pass
        else:
            i = 1/i
        x.append(i)
    return sum(x)
        
 
#피보나치 재귀njb hm 
def fib(n):
    if n==0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def test_fib(n):
    for i in range(n+1):
        print(i, fib(i))
    

#피보나치메모이제이션

def fib_memo(n):
    dic = {1:1, 2:1}

    def fib_memoization(n):
        if n in dic:
            return dic[n]
        
        dic[n] = fib_memoization(n-1) + fib_memoization(n-2)
        return dic[n]
    return fib_memoization(n)

#피보나치 제너레이터
def fibo_gen(self):
    
    def fibogenerator(n):
        a, b = 1, 1
        for n in range(n):
            yield a
            a, b = b, a + b
    def fibo_for(self):
        x = []
        for i in fibogenerator(self):
            x.append(i)
        return x[self-1]
    return fibo_for(self)
