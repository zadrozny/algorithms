#Author: Matthew Zadrozny
#Date: 2014-10-18

'''My friend David Branner posed the following questions...'''

''' Problem 1: Check whether a string contains a palindrome
and if so, return the length of the longest palindrome within
that string.
'''

tests = {
"123456789": None,  # No palindrome
"abahey": 3, 		# One palindrome
"heyaba": 3, 		# Palindrome at very end
"abcba12321": 5, 	# Two palindromes of the same length 
"abcbabcb": 7,  	# Embeded palindrome
"bcbabcba": 7,
}


def check(s):
	l = len(s)
	best = None
	for start in range(l-1):
		for end in range(start + 2, l):
			candidate = s[start:end+1]
			if candidate == candidate[::-1] and len(candidate) > 1:
				if len(candidate) > best:
					best = len(candidate)
	return best 

for test in tests:
	assert check(test) == tests[test]


'''Problem 2: Rewrite your code so that it generates all the longest substrings first, 
so that any palindrome found will necessarily be the longest'''

def check(s, min_window_length = 3):
	l = len(s)
	for window_length in range(l, min_window_length - 1, -1):
		for start_index in range(l - window_length + 1):
			candidate = s[start_index:window_length + start_index]
			if candidate == candidate[::-1]:
				return window_length
	else:
		return None 

for test in tests:
	assert check(test) == tests[test]
