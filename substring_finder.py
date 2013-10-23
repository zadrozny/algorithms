#Takes a string and extracts the longest sequence with two letters

test = 'banana'

def get_substring(string):
	if len(string) < 2:
		return 'Enter a string with 2+ characters'
	elif len(string) == 2 and string[0] != string[1]:
		substrings = [string]
		return substrings
	else: 
		string = string + 'd' #Dummy letter to catch final pairs, eg, 'ad' in 'fad'
		substrings = []
		last_char = ''
		for i, char in enumerate(string):
			if char != last_char: #Start new 'window'
				candidate = char 
				char_one = char 
				char_two = ''
				for sub_char in string[i+1:]:
					if sub_char == char_one:
						candidate += sub_char
					elif sub_char != char_one and char_two == '':
						char_two = sub_char 
						candidate += sub_char 
					elif sub_char == char_two:
						candidate += sub_char
					elif sub_char != char_one and sub_char != char_two: 
						substrings.append(candidate)
						break 
			last_char = char 

		if len(substrings) == 0:
			return 'This string has no substrings containing two characters.'
		
		else:
			return substrings

print get_substring(test)