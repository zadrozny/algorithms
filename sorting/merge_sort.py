from random import shuffle
test_list = range(100)
shuffle(test_list)

def partition(a_list):
	#Partition original list into lists of lists, each with one element
	#Can this be sped up by creating a new list?
	for i, val in enumerate(a_list):
		a_list[i] = [val]
	return a_list

def merge_two(a, b):
	#Takes two lists, a and b, each of which is already (!) ordered 
	#from smallest to largest--and merges them into one, also ordered
	#from smallest to largest.'''

	#For efficiency, reverse the lists (rather than pop from left)
	a.reverse()
	b.reverse()

	left, right = a.pop(), b.pop()

	merged_list = [] 

	while isinstance(left, (int, float)) and isinstance(right, (int, float)):
		if left <= right:
			merged_list.append(left)
			try: 
				left = a.pop()
			except IndexError: 
				left = None 
				merged_list.append(right)
				b.reverse()
				merged_list.extend(b)

		elif left > right:
			merged_list.append(right)
			try: 
				right = b.pop()
			except	IndexError:
				right = None
				merged_list.append(left)
				a.reverse()
				merged_list.extend(a)

	return merged_list

def merge_sort(a_list):
	#1. Partition the list into a list of lists, each with one element
	a_list = partition(a_list)

	#2. Merge these lists until there is only one
	while len(a_list)>1: 
		merged = [] 
		#Take two lists that are side by side
		for i, val in enumerate(a_list):
			if i%2 == 0:
				try: 
					union = merge_two(a_list[i], a_list[i+1])
					#Iterate over two lists, merging them from smallest to largest
					merged.append(union)

				#When the list has an odd number of items, merge the last item of the current list (a_list) with the last item of the merged list
				except IndexError: 
					appendage = merge_two(a_list[i], merged[-1])
					merged[-1] = appendage
		a_list = merged
	return a_list[0]

print merge_sort(test_list)
