#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Siddharth Chaphekar
# Created Date: 07/31/2023
# version ='1.0'
# ---------------------------------------------------------------------------

# PROBLEM STATEMENT: A number is considered perfect if its digits sum up to exactly 10. 
# For a positive integer n, return the n-th perfect number.

# For example, given 1, you should return 19. Given 2, you should return 28.

def find_perfect_number(n):

	total_count = 0

	for i in range(1,n):
		i = str(i)
		total = 0

		for digit in i:
			total += int(digit)

		if total == 10:
			total_count += 1

		if total_count == n:
			return i

	return -1


print(find_perfect_number(1))
print(find_perfect_number(2))


