# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 15:44:02 2023

@author: jason.smith2
"""

def merge(X, Y):
    """
    In: two sorted lists X and Y
    Out: a list of length len(X)+len(Y) with sorted elements
    """
    new = []
    X_ptr = 0
    Y_ptr = 0
    while X_ptr < len(X) and Y_ptr < len(Y):
        if X[X_ptr] < Y[Y_ptr]:
            new.append(X[X_ptr])
            X_ptr += 1
        else:
            new.append(Y[Y_ptr])
            Y_ptr += 1
    if X_ptr < len(X):
        new += X[X_ptr:]
    else:
        new += Y[Y_ptr:]
    return new

#print(merge([9], [5]))  

def merge_sort(X):
    if len(X) == 1:
        return X
    else:
        return merge(merge_sort(X[:len(X)//2]), merge_sort(X[len(X)//2:]))

