# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 11:30:41 2021

@author: LeeHoonGi
"""
import numpy as np
import matplotlib.pyplot as plt

def minkowski_dist(v1, v2, p):
    """
    Parameters
    ----------
    v1 ,v2 : equal-length arrays of numbers
        DESCRIPTION.
        
    Returns
    -------
    p : Minkowski distance of order p between v1 and v2

    """
    dist = 0.0
    
    for i in range(len(v1)):
        dist += abs(v1[i] - v2[i])**p
      
    ret = dist**(1/p)
    return ret

class Animal(object):
    def __init__(self, name, features):
        self.name = name
        self.features = np.array(features)
        
    def get_name(self):
        return self.name
    
    def get_features(self):
        return self.features
    
    def distance(self, other):
        return minkowski_dist(self.get_features(), other.get_features(), 2)

def compare_animals(animals, precision):
    """Assumes animals is a list of animals, precision an int >= 
    Builds a talbe of Euclidean distance between ecah animal"""
    #Get labels for columns ans rows
    columnLabels = []
    for a in animals:
        columnLabels.append(a.get_name())
    rowLabels = columnLabels[:]
    tableVals = []
    #Get distances between pairs of animals
    #For each row
    for a1 in animals:
        row = []
        #For each column
        for a2 in animals:
            distance = a1.distance(a2)
            if a1 == a2:
                row.append(str(round(distance, precision)))
            else:
                
                row.append(str(round(distance, precision)))
        tableVals.append(row)
    #Produce table
    table = plt.table(rowLabels = rowLabels,
                        colLabels = columnLabels,
                        cellText = tableVals,
                        cellLoc = 'center',
                        loc = 'center',
                        colWidths = [0.2]*len(animals))

    plt.axis('off')
    table.scale(1, 2.5)


Rattlesnake = [1,1,1,1,0]
Boa_constrictor = [0,1,0,1,0]
Dart_frog = [1,0,1,0,4]

rattlesnake = Animal('rattlesnake', [1,1,1,1,0])
boa = Animal('boa', [0,1,0,1,0])
dart_frog = Animal('dart frog', [1,0,1,0,4])
animals = [rattlesnake, boa, dart_frog]
alligator = Animal('alligator', [1,1,0,1,4])
animals.append(alligator)
compare_animals(animals, 3)