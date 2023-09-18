# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 23:33:09 2021

@author: LeeHoonGi
"""
from ch_10_person import *
class Politician(Person):
    """ A politician is a person who can belong to a
    political party""" 
    def __init__(self, name, party = None):
        """name and party are strings"""
        super().__init__(name)
        self.party = None
        
    def get_party(self):
        """returns the party to which self belongs"""
        return self.party
    
    def might_agree(self, other):
        """returns True if self and other belong to the same
        part or at least one of then does not belong to a
        party"""
        if self.party == None and other.party == None:
            return False
        else:
            return True
            
x = Politician('Mark Guttag')
y = Politician('Billy Bob Beaver')
x.party = 'demo'

            
        
            