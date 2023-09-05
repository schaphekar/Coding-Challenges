#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Siddharth Chaphekar
# Created Date: 08/29/2023
# version ='1.0'
# ---------------------------------------------------------------------------

# PROBLEM STATEMENT: Given an even number (greater than 2), return two prime numbers whose sum will be equal to the given number.

# A solution will always exist. See Goldbach’s conjecture.

# Example: Input: 4, Output: 2 + 2 = 4
# If there are more than one solution possible, return the lexicographically smaller solution.

# If [a, b] is one solution with a <= b, and [c, d] is another solution with c <= d, then [a, b] < [c, d] if a < c OR a==c AND b < d.

def main():
	number = int(input("Enter an even number greater than 2: "))
	prime_sum(number)

def prime_sum(number):

	if number == 0 or number == 2 or number % 2 != 0:
		print("You must enter an even number greater than 2.")

	else:
		# Generate combinations of two numbers summing to the number
		nums = {}

		i = 1

		while (i < number):
			if is_prime(i) == True and is_prime(number-i) == True and i not in nums.values():
				nums[i] = number - i
			i += 1

		# Print the dictionary
		print("Number pairs that sum to", number, "->", nums)

		# From the summing pairs, find the lexicographically smallest solution
		print("Lexicographically smallest solution ->" , nums.get(min(nums)))


def is_prime(n):

	# 1 is always composite
	if n == 1:
		return False

	# 2 is composite since only 1 and 2 are factors
	elif n == 2:
		return False

	# Odd numbers between 2 and 9
	elif n > 2 and n < 9 and n % 2 != 0:
		return True

	else:
		# Even numbers greater than 2
		if n % 2 == 0:
			return False

		else:
			# Number is perfectly divisible by single-digit odd numbers
			if n % 3 == 0 or n % 5 == 0 or n % 7 == 0 or n % 9 == 0:
				return False

			else:
				return True


if __name__ == "__main__":
	main()
