#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Siddharth Chaphekar
# Created Date: 09/13/2023
# version ='1.0'
# ---------------------------------------------------------------------------

# Problem statement: Given a string consisting of the letters x and y, such as xyxxxyxyy, and an operation called flip, which changes a single x to y or vice versa. 
# Determine how many times you would need to apply this operation to ensure that all x's come before all y's. 

# In the preceding example, it suffices to flip the second and sixth characters, so you should return 2.

# Modification: Allowing for any two characters to be compared, and allow non-target characters to be present in input.

def count_flips(string, char1, char2):

	# Validate string input
	if char1 not in string or char2 not in string or len(char1) != 1 or len(char2) != 1:
		raise ValueError("Characters either not found or invalid for input string.")
		return -1

	# Case where both target chars are the same
	if char1 == char2:
		return 0

	# Initialize count and index
	count = 0
	index = 0
	result = ""

	# Algorithm: Iterate through string, and compare the two ends of the string to decide whether or not to flip
	while index < len(string)//2:

		left_pointer = string[index]
		right_pointer = string[-1-index]

		# If the left side character needs to be flipped, increment the count
		if left_pointer == char2:
			count += 1
			left_pointer = char1

		# If the right side character needs to be flipped, increment the count
		if right_pointer == char1:
			count += 1
			right_pointer = char2

		# Update the result string by inserting into middle
		middle_index = len(result) // 2
		left_half = result[:middle_index]
		right_half = result[middle_index:]
		result = left_half + left_pointer + right_pointer + right_half

		index += 1

	# Return the final count
	print(string, "--->", result, count)
	return count


# Test cases
count_flips("hodelwwyxhodel", "x", "y")
count_flips("xyxxxyxyy", "x", "y")
count_flips("zorg!!zghz!", "!", "z")

