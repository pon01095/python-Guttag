# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 18:48:09 2021

@author: pon01
"""

# baseball_teams = {'Dodgers', 'Giants', 'Padres', 'Rockies'}
# football_teams = {'Giants', 'Eagles', 'Cardinals', 'Cowboys'}
# baseball_teams.add('Yankees')
# football_teams.update(['Patriots', 'Jets'])
# print(baseball_teams)
# print(football_teams)

class Father(object):
    def __init__(self, value):
        self.value = value
        return print(value)
    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return self.value == other.value
        else:
            return NotImplemented
        
    def __hash__(self):
        return hash(self.value)

class Son(Father):
    def __init__(self, value):
        super().__init__(value)
        
        
# if __name__ == "__main__": #원하는 모듈만 클래스에서 가져오기
a = Father("hello")
b = Son("hello")
c = set() 
c.add(a); c.add(b)
print(a==b)
    
# month_numbers = {'Jan':1, 'Feb':2, 'Mar':3, 'Apr':4, 'May':5, 1:'Jan', 2:'Feb', 3:'Mar', 4:'Apr', 5:'May'}
# print(month_numbers)
# print('The third month is ' + month_numbers[3])
# dist = month_numbers['Apr'] - month_numbers['Jan']
# print('Apr and Jan are', dist, 'months apart')

