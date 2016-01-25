#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Laakman_1_1.py

"""
Laakman: 1.1: Implement an algorithm to determine 
if a string has all unique characters. 
What if you can not use additional data structures?
"""


unique      = "abcdefghijk"
not_unique  = "abccdefghijk"


def test_uniqueness(s):
    '''Determines whether a string has all unique characters --
    without using additional data structures.'''
    for i, char in enumerate(s): 
        for subchar in s[i+1:] :
            if subchar == char:
                return "Not unique"
    return "Unique"

# Tests

assert test_uniqueness(unique) == 'Unique'
assert test_uniqueness(not_unique) == 'Not unique'



# --------------------------------------------------------------


# Using additional data structure

def test_uniqueness(s):
    '''Determines whether a string has all unique chars,
    using additional data structure: sets.'''

    if len(set(s)) == len(s):
        return 'Unique'
    else:
        return 'Not unique'

# Tests

assert test_uniqueness(unique) == 'Unique'
assert test_uniqueness(not_unique) == 'Not unique'