#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun July 30 2023

@author: siddharthchaphekar
"""

# Classic FizzBuzz implementation in which given a maximum number N, we print all numbers up to AND including N such that:
# 	- If the number is perfectly divisible by 3 and 5, then print "FizzBuzz" instead of the number
#	- If only divisible by 3 and not 5, print "Fizz"
#	- If only divisible by 5 and not 3, print "Buzz"
#	- If divisible by neither, print the number itself

# Note: This function uses "continue" statements that skip to the next iteration, but we can also use "if ... else" with multiple "if else" instead.

def main():
	number = int(input("Enter the upper limit for FizzBuzz: "))
	doFizzBuzz(number)

def doFizzBuzz(number):
	for n in range(1, number+1):

		if n % 3 == 0 and n % 5 == 0:
			print("FizzBuzz")
			continue;

		if n % 3 == 0 and n % 5 != 0:
			print("Fizz")
			continue;

		if n % 3 != 0 and n % 5 == 0:
			print("Buzz")
			continue;

		else:
			print(n)


if __name__ == "__main__":
	main()