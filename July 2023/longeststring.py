#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Siddharth Chaphekar
# Created Date: 07/19/2023
# version ='1.0'
# ---------------------------------------------------------------------------

# Inputs: A list of strings (1), and a string (2). 
# Output: Return a list of the longest strings in (1) that are each a subsequence of (2). 

# Definition: String S1 is a subsequence of S2 if some number of characters (possibly 0) can be deleted from S2 to form S1 

# Assertion: Subsequence must be constructed WITHOUT reordering the remaining characters.

arr = ["ale", "apple", "bale", "kangaroo", "apply"]
s = "abpppleey"

def main():
	list_subsequence_strings(arr,s)

def list_subsequence_strings(arr, s):
    results = []
    try:
        # Iterate over every word in the input set
        for word in arr:
            print("Doing " , word)
            idx = 0
            # Iterate over every letter in the word
            for letter in word:
                # Find the index of the first occurrence of the letter
                if letter in s:
                    idx = s.index(letter)
                    
                else:
                    print("Letter not found, so substring not possible.")
                    break
                # Reduce search string to substring depending on new idx
                sub_s = s[idx:]
                
                if letter == word[-1]:
                    results.append(word)
                    
    except ValueError:
        pass
        
    print("Results ", results)


if __name__ == '__main__':
	main()
