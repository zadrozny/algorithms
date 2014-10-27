TIMINGS

n = 10: 100000 loops, best of 3: 9.89 usec per loop
n = 100: 10000 loops, best of 3: 66.6 usec per loop
n = 1000:   10 loops, best of 3: 589 usec per loop
n = 10000:  10 loops, best of 3: 5.81 msec per loop

TIMEIT CODE
python -m timeit -s '''
import insertion_sort as test
''' '''
test.test_speed(test.list_10)'''

#where test.n == a list of cardinality n in descending order