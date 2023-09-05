#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Siddharth Chaphekar
# Created Date: 09/05/2023
# version ='1.0'
# ---------------------------------------------------------------------------

# Problem Statement: You are given a list of data entries that represent entries and exits of groups of people into a building. 
# An entry with Unix timestamp looks like this:

# {"timestamp": 1526579928, count: 3, "type": "enter"} -> this means 3 people entered the building. 

# An exit looks like this:

# {"timestamp": 1526580382, count: 2, "type": "exit"} -> this means that 2 people exited the building. 

# Find the busiest period in the building, that is, the time with the most people in the building. 
# Return it as a pair of (start, end) timestamps.

# You can assume the building always starts off and ends up empty, i.e. with 0 people inside.

# Modification: My implementation reads a JSON file to get the entries.

# Assumption: Input file record timestamps are chronologically listed/pre-sorted.

import sys
import json

from datetime import datetime

# Defines a record for the input file
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

	# Validate arguments for input json file
	num_args = len(sys.argv)

	if (num_args < 2):
		print(">>> Not enough arguments provided, need to specify an input JSON file.")
		return

	elif (num_args > 2):
		print(">>> Too many arguments provided, need to specify one input JSON file.")
		return

	records = InputFile(sys.argv[1])

	# Read the data
	data = read_entries(records)

	# Process dictionary structure
	result = find_busiest_period(data)

	# Print the tuple of start/end timestamps
	print(result)

# Function to read JSON of 
def read_entries(records):
	with open(InputFile.get_input_loc(records), 'r') as f:
		data = json.load(f)

	return data


# Function to calculate the max occupancy
def find_busiest_period(entries):

	# Tracking variables to hold time and occupancy info
	start_time = 0
	end_time = 0
	max_count = 0
	current_occupancy = 0

	for index, entry in enumerate(entries):

		# Depending on the entry type, add or subtract from the current occupancy
		if entry["type"] == "enter":
			current_occupancy += entry["count"]

		else:
			current_occupancy -= entry["count"]

		# If the current occupancy exceeds the previously recorded max, update the max
		if current_occupancy > max_count:
			max_count = current_occupancy
			start_time = entry["timestamp"]

			if index < len(entries):
				end_time = entries[index]["timestamp"]
			else:
				end_time = entries[index]["timestamp"]

	return (max_count, unix_to_readable(int(start_time)), unix_to_readable(int(end_time)))

# Helper function to convert Unix datetime to readable time
def unix_to_readable(unix_timestamp):
    try:
        # Convert the Unix timestamp to a datetime object
        timestamp = datetime.utcfromtimestamp(unix_timestamp)
        
        # Format the datetime object as a readable string
        readable_time = timestamp.strftime('%Y-%m-%d %H:%M:%S UTC')
        
        return readable_time
    
    except ValueError:
        return "Invalid timestamp"


if __name__ == "__main__":
	main()