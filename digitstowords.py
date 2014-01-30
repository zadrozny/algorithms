'''
Given the integer 123, return "one", "two", "three", 
without converting this to a string.
'''

d = {1: 'one', 2: 'two', 3: 'three'}

def convert(n):
	words = []
	i = 0
	while n / 10**i > 0: 
		conversion = d[(n / 10**i) % 10]
		words.append(conversion)
		i += 1
	return ', '.join(words[::-1])

print convert(123)