#Laakman_1_4.py

'''Laakman 1.4: Write a method to decide if two strings are anagrams or not.'''


s1 = 'abce'
s2 = 'abec'


def detect_anagram(string_one, string_two):
	if len(string_one) != len(string_two):
		return "Not anagrams"
	else: 
		s1 = [char for char in string_one]
		s2 = [char for char in string_two]
		s1.sort()
		s2.sort()
		if s1 == s2:
			return "Anagrams"
		else: 
			return "Not anagrams"

print detect_anagram(s1, s2)