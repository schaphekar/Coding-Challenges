#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 31 13:15:49 2022

@author: siddharthchaphekar
"""

# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. 
# If our input was [3, 2, 1], the expected output would be [2, 3, 6].

import time

# Brute force solution using repeated passes of original array
def getProductArray(arr):
    
    print("BRUTE FORCE")
    
    start = time.time()
    
    arr2 = []
    
    for i in arr:
        prod = 1
        for j in arr:
            if j != i:
                prod = prod * j
        arr2.append(prod)
           
    end = time.time()
    print("Took " + str(end - start) + " seconds")
    print(arr2)
    
    return arr2
        
        
def getProductArrayWithDivision(arr):
    
    print("WITH DIVISION")
    
    start = time.time()
    
    products = []
    arr2 = []
    
    for i in arr:
        print("")
        
    
    end = time.time()
    print("Took " + str(end - start) + " seconds")
    print(arr2)
    
    return arr2

def getProductArrayOptimized(arr):
    
    print("OPTIMIZED")
    
    start = time.time()
    
    n = len(arr)
    i, prod = 1, 1

    arr2 = [1 for i in range(n)]
 
    # Left-hand side of arr[i], exlcuding arr[i]
    for i in range(n):
        arr2[i] = prod
        prod *= arr[i]
 
    prod = 1
 
    # Right-hand side of arr[i], excluding arr[i]
    for i in range(n - 1, -1, -1):
        arr2[i] *= prod
        prod *= arr[i]
 

    end = time.time()
    print("Took " + str(end - start) + " seconds")
    print(arr2)
    
    return arr2
            
        
getProductArray([30,22,17,6])
getProductArrayWithDivision([30,22,17,6])
getProductArrayOptimized([30,22,17,6])


    
    