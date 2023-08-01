#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Siddharth Chaphekar
# Created Date: 08/01/2023
# version ='1.0'
# ---------------------------------------------------------------------------

# Classic Wordle solver agent implementation
# This function is non-deterministic because of the random choice of guessed words.
# Given enough guesses, a solution will always be eventually found for a valid goal word.
# But a solution may NOT be necessarily found for multiple runs of the same word with the same maximum guesses allowed.

# Library imports
from english_words import english_words_set
import random

# Defining Wordle constraints
word_length = 5
max_num_guesses = 6

# Narrow down search space to words that follow above length constraint, do not contain special characters, and are not proper nouns
english_words_set = [word for word in english_words_set if len(word) == word_length and "." not in word and "'" not in word and word[0].isupper() == False]

def wordle_guesser(max_num_guesses, goal_word, word_set):
    
    guessed_words = []
    
    # Randomly attempt a five-letter guess word
    guess_word = random.choice(list(english_words_set))
    guessed_words.append(guess_word)
    print("First guess is " + guess_word)
    guesses = 1
    
    # In the unlikely event that the random guess is correct
    if guess_word == goal_word:
            print("Amazing! Wordle solved in just one guess!")
            print("The odds of this occurring were 1 in " + str(len(english_words_set)) + " !")
            return

    while guesses < max_num_guesses:
        
        if guess_word != goal_word:
            matches = letter_match(guess_word, goal_word)
            
            # If none of the letters in the previous guess were present
            if len(matches) == 0:
                guess_word = random.choice(list(english_words_set))
                guessed_words.append(guess_word)
                
                print("Next guess is " + guess_word)
                guesses += 1
                
                if guess_word == goal_word:
                    print("Solved the Wordle in " + str(guesses) + " guesses!")
                    return
                
                
            else:
                matching_letters = [match[0] for match in matches]
                print("Perfect letter matches: " + str(matching_letters))
                
                matching_indexes = [match[1] for match in matches]
                print("Perfect letter match indexes " + str(matching_indexes))
                
                existing_letters = letters_present(guess_word, goal_word)
                print("Existing letter matches: " + str(existing_letters))
                
                english_words_subset = [word for word in english_words_set if add_word_to_subset(word, matching_letters, matching_indexes) and all([char in word for char in existing_letters]) == True and word not in guessed_words]
                guess_word = random.choice(list(english_words_subset))
                guessed_words.append(guess_word)
                
                print("Remaining possible matches: " + str(len(english_words_subset)) + " " + str(english_words_subset))
                print("Next guess is " + guess_word)
                
                guesses += 1
                
                if guess_word == goal_word:
                    print("Solved the Wordle in " + str(guesses) + " guesses!")
                    return
        
    print("Failed to solve Wordle within " + str(max_num_guesses) + " tries.")
    
    
def letter_match(word1, word2):
    
    # Store matching letters and corresponding indices
    matches = []
    
    for x, y in zip(word1, word2):
        if x == y:
            matches.append([x, word1.index(x)])
            
    return matches
        

def letters_present(word1, word2):
    
    # Store letters if they occur
    matches = []
    
    for x in word1:
        if x in word2:
            matches.append(x)
            
    return matches


def add_word_to_subset(word, matches, indexes):

    # Helper function to narrow down search space to only those words that have matches relative to the previous guess
    for x, y in zip(matches, indexes):
        if word[y] != x:
            return False
        
    return True

# Sample runs
wordle_guesser(max_num_guesses, "tango", english_words_set)
    