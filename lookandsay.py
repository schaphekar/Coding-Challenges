#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed July 27 2023

@author: siddharthchaphekar
"""

# PROBLEM STATEMENT: "Look and Say"
# A sequence that begins with the number 1, with each subsequent term describing the digits appearing in the previous term.
# Example: 1 -> 11 -> 21 -> 1211 -> 111221
# The fourth term is derived from the fact that the third term has one 1, then one 2, then two 1s

n = 5

def get_look_and_say(n):
    print(1)
    term = 1
    i = 1
    
    # Do n-1 iterations
    while i < n+1:
        term = translate(term)
        print(term)
        i += 1
        
def translate(number):
    string = str(number)
    counts = ""
    
    # Go over each digit in the string, updating the count as a new digit is encountered
    current_digit = string[0]
    count = 0

    for index, digit in enumerate(string):
        
        # If working with the same digit, add to the count
        if digit == current_digit:
            count += 1
        
        # If moved on to a new digit, append the previous digit/count and reset counter
        else:
            counts += str(count)
            counts += current_digit
            current_digit = digit
            count = 1
            
        # If reached end of string, append the current digit info and end the loop
        if index == len(string)-1:
            counts += str(count)
            counts += str(digit)
            break
    
    return counts
    
# Test look and say
get_look_and_say(n)