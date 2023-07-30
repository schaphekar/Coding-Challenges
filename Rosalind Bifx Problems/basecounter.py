#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Siddharth Chaphekar
# Created Date: 07/18/2023
# version ='1.0'
# ---------------------------------------------------------------------------

# Rosalind Bioinformatics Stronghold Problem #1: Counting DNA nucleotides
# Inputs: A file containing a list of DNA sequences
# Output: Counts for each type of nucleotide

# Modifications: Solution includes accomodation for RNA and protein sequences
# Assumptions: 

import re
import sys
import typing

USAGE_STR = "python basecounter.py <inputfile>"

DNA_BASES = {"A" : "Adenine", "C" : "Cytosine", "G" : "Guanine", "T" : "Thymine"}

RNA_BASES = {"A" : "Adenine", "C" : "Cytosine", "G" : "Guanine", "U" : "Uracil"}

AMINO_ACIDS = {"A" : "Alanine", "R" : "Arginine", "N" : "Asparagine", "D" : "Aspartic Acid", "C" : "Cysteine", "Q" : "Glutamine", "E" : "Glutamic Acid", 
"G" : "Glycine", "H" : "Histidine", "I" : "Isoleucine", "L" : "Leucine", "K" : "Lysines", "M" : "Methionine", "F" : "Phenylalanine", "P" : "Proline",
"S" : "Serine", "T" : "Threonine" "W" : "Tryptophan", "Y" : "Tyrosine", "V" : "Valine"}

### Defines a file record for inputs
class InputFile:
	def __init__(self, input_loc: str):
		"""Create a new input file record.

		Args:
		input_loc: String path to the input file.
		"""
		self._input_loc = input_loc

	def get_input_loc(self) -> str:
		return self._input_loc

def main():

	# Validate input arguments
	num_args = len(sys.argv)

	if (num_args < 1):
		print(">>> Not enough arguments provided, use the command format below:")
		print(USAGE_STR)
		return

	if (num_args > 2):
		print(">>> Too many arguments provided, use the command format below:")
		print(USAGE_STR)
		return

	sequence_file = InputFile(sys.argv[1])

	sequences = read_sequences(sequence_file)
	if get_type(sequences) == "dna":
		count_dna_bases(count_letters(sequences))

	else:
		count_protein_residues(count_letters(sequences))

def get_type(sequences):
	dna_pattern = re.compile(r'^[ACGT]+$')
	rna_pattern = re.compile(r'^[ACGU]+$')
	protein_pattern = re.compile(r'^[ACDEFGHIKLMNPQRSTVWY*-]+$')

	if dna_pattern.match(sequences[0]):
		return "dna"

	if dna_pattern.match(sequences[0]):
		return "rna"

	if protein_pattern.match(sequences[0]):
		return "protein"

	else:
		return "unknown"


def read_sequences(input1: typing.Iterable[InputFile]):
	loc = InputFile.get_input_loc(input1)

	sequences = []

	with open(loc, 'r') as f:
		data = f.read().splitlines()

	for line in data:
		if line[0] != ">":
			sequences.append(line)

	return sequences

def count_letters(seqs):
	counts = {}
	for seq in seqs:
		for nuc in seq:
			if nuc.upper() not in counts:
				counts[nuc.upper()] = 0

			counts[nuc.upper()] += 1

	return counts

def count_dna_bases(counts):
	for base in DNA_BASES.items():
		print("Total ", base, "s ", counts.get(base))

def count_rna_bases(counts):
	for base in RNA_BASES.items():
		print("Total ", base, "s ", counts.get(base))

def count_protein_residues(counts):
	for residue in AMINO_ACIDS.items():
		print("Total ", residue, "s ", counts.get(residue))

if __name__ == '__main__':
	main()
