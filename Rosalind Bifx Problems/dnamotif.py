#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Siddharth Chaphekar
# Created Date: 07/30/2023
# version ='1.0'
# ---------------------------------------------------------------------------

# Given two strings s and t, t is a substring of s if t is contained as a contiguous collection of symbols in s.
# As a result, t must be no longer than s.

# The position of a symbol in a string is the total number of symbols found to its left, including itself. 
# e.g. the positions of all occurrences of 'U' in "AUGCUUCAGAAAGGUCUUACG" are 2, 5, 6, 15, 17, and 18). The symbol at position i of s is denoted by s[i].

# Rosalind Bioinformatics Stronghold Problem #5: Finding Motifs in DNA
# Given: Two DNA strings s and t, each of length at most 1 kbp
# Return: All locations of t as a substring of s.

import unittest

def find_motif_locations(s1, s2):

	if len(s2) > len(s1):
		raise ValueError("Target motif DNA length is greater than sequence to be searched.")

	i = 0
	motif_length = len(s2)
	locations = []

	while i < len(s1)-motif_length:

		# Compare every subsequence with the n-mer window, where n is equal to the length of the motif
		if s1[i:i+motif_length] == s2:
			# Add 1 before appending to convert from 0-based indexing to 1-based positions
			locations.append(i+1)

		i += 1

	return locations

class TestHammingDistance(unittest.TestCase):
    def test_find_motif_locations(self):
        
        # Test cases with equal length strings
        self.assertEqual(len(find_motif_locations("GATATATGCATATACTT", "ATAT")), 3)   # 3 instances
        self.assertEqual(len(find_motif_locations("GATATATGCATATACTT", "TAT")), 3)    # 3 instances

        # Test cases with string length comparison
        with self.assertRaises(ValueError):
            find_motif_locations("AGTCA", "AGTCCATG")

if __name__ == "__main__":
    unittest.main()
