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



#Using collections, a la http://stackoverflow.com/a/9835819/1366410
import collections
def find_duplicates_3(lst):
	return [x for x, y in collections.Counter(lst).items() if y > 1]



if __name__ == '__main__':

	tests = {
	(1, 2, 3, 4, 5, 5, 6, 6): [5, 6],
	(1, 2, 3, 4, 5, 6, 5): [5]
	}


	for test in tests:
		assert find_duplicates_1(test) == tests[test]
		assert find_duplicates_2(test) == tests[test]
		assert find_duplicates_3(test) == tests[test]


	import timeit

	print(timeit.timeit("for x in range(10, 11): find_duplicates_1(range(x))", 
		setup="from __main__ import find_duplicates_1"))

	print(timeit.timeit("for x in range(10, 11): find_duplicates_2(range(x))", 
		setup="from __main__ import find_duplicates_2"))

	print(timeit.timeit("for x in range(10, 11): find_duplicates_3(range(x))", 
		setup="from __main__ import find_duplicates_3"))

