# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 03:36:21 2021

@author: LeeHoonGi
"""

class Account:
    def __init__(self, name, money):
           self.user = name
           self.__balance = money
    
    def __get_balance(self):
        return self.__balance
    
    def __set_balance(self, money):
        if money < 0:
            return
        self.__balance = money
    
# if __name__ == '__main__':
#     my_acnt = Account("greg", 5000)
#     my_acnt.__balance = -3000
    
#     print(my_acnt.get_balance())
#     print(my_acnt.set_balance(6000))
#     print(my_acnt.get_balance())
#     print(my_acnt.__dict__)
    
class Person(Account):
    pass
    # def __init__(self, name, money):
    #    super().__init__(name, money)
       
    #    @property
    #    def money(self):
    #       super().__get_balance(self)
    #       return self.__balance 
           
    #       # print('getter executed')
    #        # self.__money = money
    
    #    @money.setter
    #    def __money(self, money):
    #       super().__set_balance(self, money)
    #       if money < 0:
    #           print("음수보다 큰 값을 넣어주세요")
    #           return
          
    #       self._money = money    

if __name__ == "__main__":
    john = Person('john' , 5000)
    print(john.__dict__)
    