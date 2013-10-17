from random import choice, shuffle
l = range(-110, 110)
shuffle(l)

def quick_sort(seq):
	if len(seq) <= 1:	#base case 
		return seq
	else: 	
		"""Pick an element, called a pivot, from the list."""
		pivot = choice(seq)
		"""Reorder the list so that all elements with values less than the pivot 
		come before the pivot, 		while all elements with values greater than 
		the pivot come after it (equal values can go either way). After this partitioning, 
		the pivot is in its final position. This is called the partition operation."""
		less = []
		more = []
		for n in seq:
			if n < pivot:
				less.append(n)
			else: #so pivot itself gets appended to the more
				more.append(n)

		"""Recursively apply the above steps to the sub-list of elements with 
		smaller values and separately the sub-list of elements with greater values."""
		less = quick_sort(less)
		more = quick_sort(more)

		seq = less + more 

		return seq

print quick_sort(l)