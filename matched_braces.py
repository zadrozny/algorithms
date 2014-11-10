'''
Challenge 2: Braces

Given an array of strings containing three types of braces: round (), square [] and curly {}

Your task is to write a function that checks whether the braces in each string are correctly matched prints 1 to standard output (stdout) if the braces in each string are matched and 0 if they're not (one result per line)

Note that your function will receive the following arguments:
expressions which is an array of strings containing braces

Data constraints:
the length of the array will not exceed 100
the length of any string will not exceed 5000

Efficiency constraints
your function is expected to print the result in less than 2 seconds

Example
Input	Output
expressions: [ ")(){}", "[]({})", "([])", "{()[]}", "([)]" ]
0
1
1
1
0
'''

def check_braces(expressions):
	open_braces = ['(', '[', '{']
	closed_braces = [')', ']', '}']
	for expression in expressions:
		print
		print expression
		q = []
		for char in expression:
			if char in open_braces:
				q.append(char)
			else:
				if len(q) == 0:
					print 0 
					break 
				elif closed_braces.index(char) != open_braces.index(q.pop()):
					print 0
					break 
		else:
			print 1


expressions = [ ")(){}", "[]({})", "([])", "{()[]}", "([)]" ]

check_braces(expressions)

