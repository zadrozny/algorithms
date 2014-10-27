TIMES

n = 10: 10000 loops, best of 3: 111 usec per loop
n = 100: 1000 loops, best of 3: 1.4 msec per loop
n = 1000: 100 loops, best of 3: 16.8 msec per loop
n = 10000: 10 loops, best of 3: 189 msec per loop

TIMEIT CODE

python -m timeit -s '''
import quick_sort as test
''' '''
test.quick_sort(test.list_10000)'''

#where test.n == a list of cardinality n in descending order