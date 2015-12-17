#!/usr/bin/python2
# -*- coding: utf-8 -*-

from random import shuffle
import itertools

def radix_sort(array, mod=10, StopIter=False):
	'''Sort a list of integers using radix sort'''
    if StopIter == True:
        return array 

    else:
        StopIter = True # Assume this is last iteration...
        container = [[] for d in range(0, 10)]

        for n in array:
            if n / mod != 0:     # ... correct if not
                StopIter = False			
			
            remainder = (n % mod) / (mod / 10)
            container[remainder].append(n)
		
        if StopIter == False: 
            mod *= 10 

        array = list(itertools.chain(*container)) # Flatten

        return radix_sort(array=array, mod=mod, StopIter=StopIter)
	

# Test:

nums = range(100)

shuffle(nums)

assert nums != sorted(nums)

assert radix_sort(nums) == sorted(nums)

