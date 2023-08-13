#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Siddharth Chaphekar
# Created Date: 08/01/2023
# version ='1.0'
# ---------------------------------------------------------------------------

# PROBLEM STATEMENT: Longest palindrome in a sequence
# Given a string s, find the longest palindrome substring within s.
# I created two implementations, one using a brute force approach and one with a more optimal solution.

import time

def find_longest_palindrome_brute_force(s):

	"""
	A simplistic and inefficient solution that:
		1) Iteratively creates all possible substrings from the input string, starting with the first character
		2) Uses those substrings to identify palindromes
		3) Finds the max length palindrome of the set

	"""

	subs = []
	palindromes = []
	largest_palindrome = ""

	# Create every possible substring within the string sequence
	for i, letter in enumerate(s):
		subs.append(generate_substrings(s[i:]))

	flatList = [item for elem in subs for item in elem]

	for word in flatList:
		if word == word[::-1] and len(word) > 1 and word not in palindromes:
			palindromes.append(word)
			if len(word) > len(largest_palindrome):
				largest_palindrome = word

	print("ALL PALINDROMES ", palindromes)
	print("LARGEST PALINDROME ", largest_palindrome)

def generate_substrings(s):
	substrings = []

	i = 0

	while i < len(s)-1:
		substrings.append(s[0:i+1])
		i += 1

	return substrings

def find_longest_palindrome_optimized(s):
	"""
	A more efficient solution that chooses a center and reads in both directions for palindromic sequences by:

		- Traversing through the string starting with i and using pointers such that prefix_index = i - 1 and suffix_index = i + 1
		- suffix_index is incremented while the substrings match
		- Then do the same for prefix_index, but decrement since we are going in the reverse direction
		- Then do increments/decrements until the two lengths match
	"""

	size = len(s)

	# If size = 0 (empty string) or size = 1 (always palindrome), simply return the string length
	if size < 2:
		return size

	start_index = 0
	maxLength = 1

	# Single pass through the string, tracking the indexes +/- 1 relative to the current index
	for i in range(size):
		prefix_index = i - 1
		suffix_index = i + 1

		# So long as the suffix_indexer index does not exceed string size, and the start and end letters are the same, keep incrementing
		while suffix_index < size and s[suffix_index] == s[i]:
			suffix_index += 1

		# So long as the prefix_indexer index is at least as large as the minimum (0), and the letters are the same, keep decrementing
		while prefix_index >= 0 and s[prefix_index] == s[i]:
			prefix_index -= 1


		# So long as both indexes fall within the string range and the characters are equal, continue increment/decrement
		while prefix_index >= 0 and suffix_index < size and s[prefix_index] == s[suffix_index]:
			prefix_index -= 1
			suffix_index += 1

		val = start_index + maxLength
		print(s[start_index:val])

		length = suffix_index - prefix_index - 1

		if maxLength > length:
			maxLength = length
			start_index = prefix_index + 1

	val = start_index + maxLength
	print("Longest palindrome substring is: ", str(s[start_index:val]))

	return maxLength

s1 = time.time()
find_longest_palindrome_brute_force("cardamombbcreatenayanbbeats")
s2 = time.time()
s3 = s2 - s1

s4 = time.time()
find_longest_palindrome_optimized("cardamombbcreatenayanbbeats")
s5 = time.time()
s6 = s5 - s4

print("Brute force: ", s3)
print("Optimized: ", s6)