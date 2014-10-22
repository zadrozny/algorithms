'''
Write a function that finds and returns
the duplicates in a list. 

Write a test for this. 
'''


def find_duplicates_1(lst):
	duplicates = []
	for element in set(lst):
		if lst.count(element) > 1:
			duplicates.append(element)
	return duplicates


#Rewritten as a list comprehension
def find_duplicates_2(lst):
	return [element for element in set(lst) if lst.count(element) > 1]


#From http://stackoverflow.com/a/9835819/1366410
import collections
def find_duplicates_3(lst):
	return [x for x, y in collections.Counter(lst).items() if y > 1]


tests = {
(1, 2, 3, 4, 5, 5, 6, 6): [5, 6],
(1, 2, 3, 4, 5, 6, 5): [5]
}


for test in tests:
	assert find_duplicates_1(test) == tests[test]
	assert find_duplicates_2(test) == tests[test]
	assert find_duplicates_3(test) == tests[test]
