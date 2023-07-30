#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Siddharth Chaphekar
# Created Date: 07/30/2023
# version ='1.0'
# ---------------------------------------------------------------------------

# Rosalind Bioinformatics Stronghold Problem #4: Hamming Distance
# Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).
# Return: The Hamming distance dH(s,t)

import unittest

def calculate_hamming_distance(s1, s2):

	if len(s1) != len(s2):
		raise ValueError("Input strings must have equal length!")

	"""
	Standard method using iterator and counter increment

	distance = 0
	for i in range(len(s1)):
		if s1[i] != s2[i]:
			distance += 1

	return distance
	"""

	# This is the most "Pythonic" way of accomplishing the same thing
	return sum(c1 != c2 for c1, c2 in zip(s1, s2))


class TestHammingDistance(unittest.TestCase):
    def test_calculate_hamming_distance(self):
        # Test cases with equal length strings
        self.assertEqual(calculate_hamming_distance("AGTCA", "AGTCA"), 0)  # Identical strings
        self.assertEqual(calculate_hamming_distance("AGTCA", "AGTCC"), 1)  # One mismatch
        self.assertEqual(calculate_hamming_distance("AGTCA", "CGTCA"), 1)  # One mismatch
        self.assertEqual(calculate_hamming_distance("AGTCA", "AGTCC"), 1)  # One mismatch
        self.assertEqual(calculate_hamming_distance("AGTCA", "CGTCC"), 2)  # Two mismatches
        self.assertEqual(calculate_hamming_distance("ACTCA", "TGAGT"), 5)  # All positions mismatch

        # Test cases with unequal length strings
        with self.assertRaises(ValueError):
            calculate_hamming_distance("AGTCA", "AGTC")
            calculate_hamming_distance("AGTCAAAACTGTACG", "")

if __name__ == "__main__":
    unittest.main()
