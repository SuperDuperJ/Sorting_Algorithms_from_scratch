# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 13:24:22 2023

@author: jason.smith2
"""

def place_pivot(X, left, right):
    pivot_index = left-1
    pivot = X[pivot_index]
    while left < right:
        # Reposition left
        while X[left] < pivot and left < len(X)-1:
            left += 1
        # Reposition right
        while X[right] > pivot and right >= 0:
            right -= 1
        # Swap
        if left < right:
            temp = X[left]
            X[left] = X[right]
            X[right] = temp
    # Place pivot
    if left != right:
        temp = X[right]
        X[right] = pivot
        X[pivot_index] = temp
    elif X[right] < pivot:
        temp = X[right]
        X[right] = pivot
        X[pivot_index] = temp
    return right

def quick_sort(X, left, right):
    if left <= right:
        pivot_location = place_pivot(X, left, right)
        quick_sort(X, left, pivot_location-1)
        quick_sort(X, pivot_location+2, right)
        
