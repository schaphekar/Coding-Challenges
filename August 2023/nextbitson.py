#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Siddharth Chaphekar
# Created Date: 08/13/2023
# version ='1.0'
# ---------------------------------------------------------------------------

# Problem Statement: Given an integer n, find the next biggest integer with the same number of 1-bits on. 
# For example, given the number 6 (0110 in binary), return 9 (1001).

def main():
	num = int(input("Enter an integer to find the next biggest integer with the same number of 1-bits on: "))
	comparator = num + 1

	# Binary equivalent
	print("Number is ",  num, "with binary equivalent ", int_to_binary(num))

	# Calculate number of 1-bits on
	ones = str(int_to_binary(num)).count("1")

	# Keep computing the binary equivalent until the bit condition is satisfied
	while True:
		binary = int_to_binary(comparator)

		print("Number is ", comparator, "with binary equivalent ", binary)

		if str(binary).count("1") == ones:
			print("*** Same number of 1-bits on found! --> Next conditional equivalent is", comparator)
			return comparator

		comparator += 1

# Helper function to convert an integer to binary
def int_to_binary(n):
	
	# Start with n and keep dividing it by 2 while tracking the quotient and the remainder
	bit_string = ""

	while n != 0:
		quotient = n//2
		remainder = n%2
		bit_string += str(remainder)
		n = quotient

	# Write out the remainders in the reverse order
	return bit_string[::-1]

# Helper function to convert a binary to integer
def binary_to_int(binary):
	
	bits = str(binary)
	result = 0

	# Iterate over each bit and calculate total
	for index, bit in enumerate(reversed(bits)):
		result += 2**(index) * int(bit)

	return result


if __name__ == "__main__":
	main()

