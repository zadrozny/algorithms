'''
Write a function that finds and returns
the duplicates in a list. 

Write a test for this. 
'''


x = [1, 2, 3, 4, 5, 5, 6, 6]

def find_duplicates(lst):
	duplicates = []
	for element in set(lst):
		if lst.count(element) > 1:
			duplicates.append(element)
	return duplicates


#Rewritten as a list comprehension
def find_duplicates(lst):
	return [element for element in set(lst) if lst.count(element) > 1]


assert find_duplicates(x) == [5, 6]
