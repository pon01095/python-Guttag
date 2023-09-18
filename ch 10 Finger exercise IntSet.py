# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 03:36:59 2021

@author: LeeHoonGi
"""

class IntSet(object):
    """An IntSet is a set of integers"""
    
    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []
        
    def insert(self, e):
        """Assumme e is an integer and inserts e into self"""
        if e not in self.vals:
            self.vals.append(e)
            
    def member(self, e):
        """Returns True if e is in self, and False otherwise"""
        return e in self.vals
    
    def remove(self, e):
        """Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + " not found")
            
    def getMembers(self):
        return self.vals[:]
    
    def __str__(self):
        self.vals.sort()
        result = ""
        for e in self.vals:
            result = result + str(e) + ","
        return "{" + result[:-1] + "}"  # -1 omits trailing comma
    
    def __eq__(self, other):
        return self.vals == other.vals
    
    def __hash__(self):
        return id(self)
    
    def __add__(self, other):
        new_IntSet = IntSet()
        new_IntSet.vals = self.vals + other.vals
        return new_IntSet
    
    # def union(self, other):
    #      """other is an Int_set
    #      mutates self so that it contains exactly the elemnts in self
    #      plus the elements in other."""
    #      try:
    #          for i in range(len(other.getMembers())):
    #              self.vals.append(other.getMembers()[i])
    #      except:
    #             raise ValueError
  
s = IntSet()
x = IntSet()
s.insert(3)
x.insert(4)