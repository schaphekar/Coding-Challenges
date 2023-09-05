#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Siddharth Chaphekar
# Created Date: 08/06/2023
# version ='1.0'
# ---------------------------------------------------------------------------

# PROBLEM STATEMENT: Pitfalls of Reversing Translation
# When researchers discover a new protein, they would like to infer the strand of mRNA from which this protein could have been translated
# This allows them to locate genes associated with this protein on the genome.

# Although any RNA string can be translated into a unique protein string, reversing the process yields a huge number of possible RNA strings from a single protein string
# This is because most amino acids correspond to multiple RNA codons i.e codon degeneracy

# Because of memory considerations, most data formats that are built into languages have upper bounds on how large an integer can be
# in some versions of Python, an "int" variable may be required to be no larger than 231−1, or 2,147,483,647. 

# As a result, to deal with very large numbers in Rosalind, we need to devise a system that allows us to manipulate large numbers without actually having to store large numbers.

# Given: A protein string of length at most 1000 aa.

# Return: The total number of different RNA strings from which the protein could have been translated, modulo 1,000,000. 
# Note: Don't neglect the importance of the stop codon in protein translation

from collections import defaultdict
from functools import reduce

rnaCodonTable = {
        # RNA codon table
        # U
        'UUU': 'F', 'UCU': 'S', 'UAU': 'Y', 'UGU': 'C',  # UxU
        'UUC': 'F', 'UCC': 'S', 'UAC': 'Y', 'UGC': 'C',  # UxC
        'UUA': 'L', 'UCA': 'S', 'UAA': '-', 'UGA': '-',  # UxA
        'UUG': 'L', 'UCG': 'S', 'UAG': '-', 'UGG': 'W',  # UxG
        # C
        'CUU': 'L', 'CCU': 'P', 'CAU': 'H', 'CGU': 'R',  # CxU
        'CUC': 'L', 'CCC': 'P', 'CAC': 'H', 'CGC': 'R',  # CxC
        'CUA': 'L', 'CCA': 'P', 'CAA': 'Q', 'CGA': 'R',  # CxA
        'CUG': 'L', 'CCG': 'P', 'CAG': 'Q', 'CGG': 'R',  # CxG
        # A
        'AUU': 'I', 'ACU': 'T', 'AAU': 'N', 'AGU': 'S',  # AxU
        'AUC': 'I', 'ACC': 'T', 'AAC': 'N', 'AGC': 'S',  # AxC
        'AUA': 'I', 'ACA': 'T', 'AAA': 'K', 'AGA': 'R',  # AxA
        'AUG': 'M', 'ACG': 'T', 'AAG': 'K', 'AGG': 'R',  # AxG
        # G
        'GUU': 'V', 'GCU': 'A', 'GAU': 'D', 'GGU': 'G',  # GxU
        'GUC': 'V', 'GCC': 'A', 'GAC': 'D', 'GGC': 'G',  # GxC
        'GUA': 'V', 'GCA': 'A', 'GAA': 'E', 'GGA': 'G',  # GxA
        'GUG': 'V', 'GCG': 'A', 'GAG': 'E', 'GGG': 'G'  # GxG
    }

dnaCodonTable = {key.replace('U', 'T'): value for key, value in rnaCodonTable.items()}

# Reverse the rna codon table by swapping key-value pairs
proteinToRNA = defaultdict(list)
for codon, aa in rnaCodonTable.items():
    proteinToRNA[aa].append(codon)

def main():

	protein = input("Enter a protein sequence: ")

	calculate_all_rna_seqs(protein)


def calculate_all_rna_seqs(protein):

	combinationList = []

	for residue in protein:
		print("Possible codons for ", residue, " -> ", proteinToRNA.get(residue))
		combinationList.append(len(proteinToRNA.get(residue)))

	result1 = reduce((lambda x, y: x * y), combinationList)

	print(combinationList)
	print(result1)


if __name__ == "__main__":
	main()

