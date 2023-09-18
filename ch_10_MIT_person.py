# # -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 22:39:53 2021

@author: LeeHoonGi
"""

from ch_10_person import *

class MIT_person(Person):
    _next_id_num = 0 #identificatoin number

    
    def __init__(self, name):
        super().__init__(name)
        self._id_num = MIT_person._next_id_num
        MIT_person._next_id_num += 1
    
    def get_id_num(self):
        return self._id_num
    
    def __lt__(self, other):
        try:
            return self._id_num < other._id_num
        except:
            return ValueError
    
    # def is_student(self):
    #     return type(self) == Grad or type(self) == UG

    
    def is_student(self):
        return isinstance(self, Student)        
    
class Student(MIT_person):
    pass

class UG(Student):
    def __init__(self, name, class_year):
        super().__init__(name)
        self.year = class_year
    
    def get_class(self):
        return self.year
    
class Grad(Student):
    pass


if __name__ == "__main__":    
    
    p1 = MIT_person('Mark Guttag')
    p2 = MIT_person('Billy Bob Beaver')
    p3 = MIT_person('Billy Bob Beaver')
    p4 = Person('Billy Bob Beaver')
    p5 = Grad('Buzz Aldrin')
    p6 = UG('Billy Beaver', 1984)
    print(p5, 'is a graduate student is', type(p5) == Grad)
    print(p5, 'is an undergraduate student is', type(p5) == UG)
    print(p5, 'is a student is', p5.is_student())
    print(p6, 'is a student is', p6.is_student())
    print(p3, 'is a student is', p3.is_student())

if __name__ == "__main__":    
        
       
    p1 = MIT_person('Mark Guttag')
    p2 = MIT_person('Billy Bob Beaver')
#     p3 = MIT_person('Billy Bob Beaver')
#     p4 = Person('Billy Bob Beaver')
    
#     print('p1 < p2 =', p1 < p2)
#     print('p3 < p2 =', p3 < p2)
#     print('p4 < p1 =', p4 < p1)
#     print('p1 < p4 =', p1 < p4)
    
    # print(str(p1) + '\'s id number is ' + str(p1.get_id_num()))
