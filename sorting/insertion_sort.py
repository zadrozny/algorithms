import random 
test_list = range(1, 1000)
random.shuffle(test_list)

def sort(a_list):
	for i, val in enumerate(a_list): 
		temp = i
		#compare with those to the the_listeft
		while temp != 0 and a_list[temp] < a_list[temp - 1]:
			a_list[temp], a_list[temp-1] = a_list[temp - 1], a_list[temp]
			temp -= 1

	return a_list 


def fill_random_list(the_range=10000):
	'''David Branner's code'''
	return [random.randint(-10000,10000) for i in range(the_range)]	

def test(x):
	test_list = fill_random_list(1000)
	assert sort(x) == sorted(x)

test(test_list)

print sort(test_list)