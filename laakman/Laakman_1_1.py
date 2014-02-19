#Laakman_1_1.py
"""Laakman: 1.1: Implement an algorithm to determine 
if a string has all unique characters. 
What if you can not use additional data structures?
"""

unique 		= "abcdefghijk"
not_unique 	= "abccdefghijk"
not_unique2 = "abcdefghijkc"


def test_uniqueness(s):
	'''Determines whether a string has all unique characters --
	without using additional data structures.'''
	for i, char in enumerate(s): 
		for subchar in s[i+1:] :
			if subchar == char:
				return "Not unique"
	else:
		return "Unique"


print test_uniqueness(unique)
print test_uniqueness(not_unique)
print test_uniqueness(not_unique2)