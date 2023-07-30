#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Siddharth Chaphekar
# Created Date: 07/19/2023
# version ='1.0'
# ---------------------------------------------------------------------------

# Rosalind Bioinformatics Stronghold Problem #2: Counting DNA nucleotides
# Inputs: A file containing a list of DNA sequences
# Output: The ID of the string having the highest GC-content, followed by the GC-content of that string.

# Modification: My solution will print all sample IDs with % GC in descending order.
# Assumption: All sequence IDs are unique, but sequences themselves can be identical.

import re
import sys
import typing
import operator

BASES = ["G", "C"]
USAGE_STR = "python highestgc.py <inputfile>"

FORMAT_CHARS = "---------------- --------------- ---------"

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

	rank_samples_gc_desc(sequences)

def calculate_gc(seq):
	gc_count = 0
	for base in seq:
		if base.upper() in BASES:
			gc_count += 1

	return round((gc_count/len(seq))*100, 2)

def rank_samples_gc_desc(sequences):

	gc_contents = {}
	
	# Calculate GC content for every sample
	for seq_id in sequences.keys():
		gc_contents[seq_id] = calculate_gc(sequences[seq_id])

	# Sort the dictionary by descending % GC
	sorted_samples = dict(sorted(gc_contents.items(), key=operator.itemgetter(1), reverse=True))

	print(FORMAT_CHARS)
	print("SAMPLE_ID	| ", "GC Content	| ", "Length |")
	print(FORMAT_CHARS)

	for s in sorted_samples:
		print(s[1:], "	| ", sorted_samples[s], "%", "	| ", len(sequences[s]), "	  |")

	print(FORMAT_CHARS)

def read_sequences(input1: typing.Iterable[InputFile]):

	headers = []
	sequences = []
	loc = InputFile.get_input_loc(input1)

	with open(loc, 'r') as f:
		data = f.read().splitlines()

	for line in data:
		if line[0] == ">":
			headers.append(line)

		else:
			sequences.append(line)

	samples = {headers[i]: sequences[i] for i in range(len(headers))}

	return samples

if __name__ == '__main__':
	main()