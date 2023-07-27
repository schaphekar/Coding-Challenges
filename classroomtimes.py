#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed July 27 2023

@author: siddharthchaphekar
"""

# PROBLEM STATEMENT:
# Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.
# For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.

# Assumption: If the end time of one block and the start time of the next are equal, this will be considered a conflict.

# If we went with the alternative assumption, then we would simply revise the conflict check by 1, i.e. if num == previous_num + 1.

time_intervals = [(30, 74), (0, 50), (60, 150), (4,177)]

def find_min_rooms_needed(arr):
    # For every interval in the range, add numbers to list
    times = []
    for interval in time_intervals:
        for x in range(interval[0], interval[1]+1):
            times.append(x)
        
    # Sort the list to simulate chronological order
    times.sort()
    
    # For all nummbers, find the frequency of each
    frequency = {}
    count = 1
    previous_num = times[0]
    
    for index, num in enumerate(times):
        
        # Check whether the last element has been reached
        if index == len(times)-1:
            frequency[num] = count
            break
        
        previous_num = times[index-1]
        
        # If the number matches previous, add to the count
        if num == previous_num:
            count += 1
            
        # If the next number is greater than previous, add previous to lookup table and proceed
        elif num > previous_num:
            frequency[previous_num] = count
            count = 1
    
    # Return the maximum # of conflicts across the entire time series
    return max(frequency.values())
    
print(find_min_rooms_needed(time_intervals))