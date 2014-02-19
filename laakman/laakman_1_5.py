#Laakman_1_5.py

'''Write a method to replace all spaces in a string with '%20'.'''


s = "I went to the park."


def replace(s):
	'''Replaces all spaces in a string with '%20'.'''
	new_string = ''
	for i, char in enumerate(s): 
		if char == " ": 
			new_string += '%20'
		else: 
			new_string += char 
	return new_string


print replace(s)