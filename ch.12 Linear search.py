# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 15:51:50 2021

@author: LeeHoonGi
"""

def search(L, e):
    """
    

    Parameters
    ----------
    L : List
        DESCRIPTION.
    e : if e in in L = True
        else: False.

    Returns True or False
    -------
    
    """
    
    for i in range(len(L)):
        if L[i] == e:
            return True
        return False
    

def search2(L, e):
    """
    

    Parameters
    ----------
    L : List
        the elements of which are in ascending oreder
        
    e : if e in in L = True
        else: False.

    Returns True or False
    -------
    
    """
    
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    
    return False

def search3(L, e):
    """
    Parameters
    ----------
    L : list
        오름차순으로 정렬된 리스트
    e : list L에서 찾고자 하는 원소

    Returns
    -------
    e가 L에 있으면 True 아니면 False
    True or False
  
    """
    
    def bin_search(L, e, low, high):
        
        #high - low 감소
        if high == low:
            return L[low] == e
        
        mid = (low + high) // 2
        
        if L[mid] == e:
            return True
        
        elif L[mid] > e:
            if low == mid:
                return False
            else:
                return bin_search(L, e, low, mid-1)
 
        else:
            return bin_search(L, e, mid + 1, high)
        
    if len(L) == 0:
        return False
    else:
        return bin_search(L, e, 0, len(L) - 1)
    
    
def selSort(L):
    """
    Parameters
    ----------
    L : List
    >, <를 이용해 비교 가능한 요소들의 리스트
    
    Returns
    -------
    L을 오름차순으로 정렬.

    """
    suffixStart = 0
    
    while suffixStart != len(L):
        
        for i in range(suffixStart, len(L)):
            if L[i] < L [suffixStart]:
                L[suffixStart], L[i] = L[i], L[suffixStart]
                
        suffixStart += 1
    return L

def merge(left, right,  compare = lambda x, y : x < y):
    """
    
    Parameters
    ----------
    left, right : List
        정렬된 리스트.
    compare : Function
        정렬방법을 명시한 함수
    Returns
    -------
    compare에 의해 새롭게 정리된 left + right 리스트.

    """
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        
        else:
            result.append(right[j])
            j += 1
    
    
    while (i < len(left)):
        result.append(left[i])
        i += 1
        
    while (j < len(right)):
        result.append(right[j])
        j += 1
        
    return result

def mergeSort(L, compare = lambda x, y : x < y):
    
    if len(L) < 2:
        return L[:]
    
    else:
        middle = len(L) // 2
        left = mergeSort(L[:middle], compare)
        right = mergeSort(L[middle:], compare)
     
        return merge(left, right, compare)
    
def last_firstName(name1, name2):
    arg1 = name1.split(' ')
    arg2 = name2.split(' ')
    if arg1[1] != arg2[1]:
        return arg1[1] < arg2[1]
    else:
        return arg1[0] < arg2[0]
    
def first_lastName(name1, name2):
    arg1 = name1.split(' ')
    arg2 = name2.split(' ')
    if arg1[1] != arg2[1]:
        return arg1[0] < arg2[0]
    else:
        return arg1[1] < arg2[1]
    
L = ['Tom Brady', 'Eric Grimson', 'Gisele Bundchen']
newL = mergeSort(L, last_firstName)
newL2 = mergeSort(L, first_lastName)

