#!/usr/bin/python2.7
# -*- coding: utf8 -*-

'''
def check_anagrams(first_words, second_words):
    # Write your code here
    # To print results to the standard output you can use print
    # Example print "Hello world!"


Two words are considered anagrams if by rearranging the letters of the first word we get the second word. For instance cinema and iceman are anagrams.
Given a list of word pairs your task is to write a function that determines for each pair if it’s an anagram or not for each pair of words your function will print to standard output (stdout) the value 1 if the pair is an anagram or 0 otherwise (one result per line)

Note that your function will receive the following arguments:
firstWords which is an array of strings giving the first word for each of the pairs secondWords which is an array of strings giving the corresponding second word 

Data constraints
the number of word pairs will not exceed 100
the maximum length of any word in the pairs will not exceed 100 characters
all words will contain only lowercase English letters (a-z)

Efficiency constraints
your function is expected to print the result in less than 2 seconds

Example
Input	Output
firstWords: “cinema”, “host”, “aba”, “train”
secondWords: “iceman”, “shot”, “bab”, “rain”
1
1
0
0
Explanation
for the given arguments above we have the following pairs:
(cinema, iceman) (host, shot) (aba, bab) (train, rain)
only the first two pairs are anagrams.
'''

from collections import Counter

def check_anagrams(first_word, second_word):
	if Counter(first_word) == Counter(second_word):
		return 1
	else:
		return 0


firstWords = 'cinema', 'host', 'aba', 'train'
secondWords = 'iceman', 'shot', 'bab', 'rain'

for pair in zip(firstWords, secondWords):
	print check_anagrams(*pair)