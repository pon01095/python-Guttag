# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 10:43:03 2021

@author: LeeHoonGi
"""
class Fruits:
    def __init__(self, name, price):
        self.price = price
        self.name = name
        
    def get_price(self):
        return print(f'Price of {self.name} is {self.price}')
    
    def get_name(self):
        return print(f'Fruit\'s name is {self.name}')

    def up(self, up):
        self.price += up

    def down(self,down):
        self.price -= down
        