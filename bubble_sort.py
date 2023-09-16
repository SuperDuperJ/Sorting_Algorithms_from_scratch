# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 14:53:19 2023

@author: jason.smith2
"""

def bubble_sort(X):
    for j in range(len(X)-1,0,-1):
        for i in range(j):
            if X[i] > X[i+1]:
                temp = X[i]
                X[i] = X[i+1]
                X[i+1] = temp
    return X

