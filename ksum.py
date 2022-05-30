#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 30 14:41:27 2022

@author: siddharthchaphekar
"""

# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, would return true since 10 + 7 = 17.
# BONUS: Single pass solution

import time

# Brute force solution using repeated passes of array
def checkTwoSumEqualsK(arr, k):
    
    print("BRUTE FORCE")
    
    start = time.time()
    
    if not arr:
        print("Empty array.")
        end = time.time()
        print("Took " + str(end - start) + " seconds")
        print("------------------------------------------------------------------")
        return False
    
    
    i = 0
    j = 1
    
    length = len(arr)
    
    # Iterate through list 
    while i < length-2:
            
        if arr[i] + arr[j] == k:
            print("True, found " + str(arr[i]), "and", arr[j], "at", "index", str(i), "and index", str(j) + "!")
            break
        
        if j == len(arr)-1:
            i += 1
            j = i+1
            
        if j == len(arr)-1 and i == j-1:
            print("Reached end of list at indexes", str(i) + " and " + str(j) + ", no two numbers adding up to", k, "found.")
            
        j += 1
    
    end = time.time()
    print("Took " + str(end - start) + " seconds")
    print("------------------------------------------------------------------")

# Single pass solution using hashing
def checkTwoSumEqualsKBonus(arr, k):
    
    print("SINGLE PASS")
    
    start = time.time()
    
    if not arr:
        print("Empty array.")
        end = time.time()
        print("Took " + str(end - start) + " seconds")
        print("------------------------------------------------------------------")
        return False
    
    nums = {}

    for i in range(len(arr)):
        complement = k - arr[i]

        if nums.get(complement) is not None:
            
            # If the pair adds up to k, we are finished here
            print("True, found ", [arr[i], arr[nums.get(complement)]], "at index", i, nums.get(complement))        
            end = time.time()
            print("Took " + str(end - start) + " seconds")
            print("------------------------------------------------------------------")
            return True
            
        # Generate a map/dictionary
        nums[arr[i]] = i
            
    end = time.time()
    
    print("No two numbers were found to sum to " + str(k))
    print("Took " + str(end - start) + " seconds")
    print("------------------------------------------------------------------")
    
# Test cases for brute force solution
checkTwoSumEqualsK([10,15,3,7], 17)

checkTwoSumEqualsK([0,5,44,2,6], 50)
checkTwoSumEqualsK([11, 6, 36, 77, 8, 10, 2, 99], 92)
checkTwoSumEqualsK([], 3)
checkTwoSumEqualsK([0,-9,66,6,14,-332, 9], -326)

# Test cases for bonus solution
checkTwoSumEqualsKBonus([10,15,3,7], 17)
checkTwoSumEqualsKBonus([0,5,44,2,6], 50)
checkTwoSumEqualsKBonus([11, 6, 36, 77, 8, 10, 2, 99], 92)
checkTwoSumEqualsKBonus([], 3)
checkTwoSumEqualsKBonus([0,-9,66,6,14,-332, 9], -326)
