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

def check_braces(expression):
	open_braces = ['(', '[', '{']
	closed_braces = [')', ']', '}']

	q = [] 

	for char in expression:
		
		if char in open_braces: # Push the stack
			q.append(char)

		else: # It's a closed brace.
			
			if len(q) == 0: # First bracket closed/extra closed brackets
				return 0 
			
			if closed_braces.index(char) != open_braces.index(q.pop()):
				return 0

	else:
		return 1


expressions = [ ")(){}", "[]({})", "([])", "{()[]}", "([)]" ]

for expression in expressions:
	print check_braces(expression)

