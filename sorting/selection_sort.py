#!/usr/bin/python2
# -*- coding: utf-8 -*-

from random import shuffle

def selection_sort(array, index=0):
    '''Sort a list of integers using selection sort'''
    if index == len(array):
        return array
    else:
        smallest    = None
        current     = None

        for i, e in enumerate(array[index:]):
            if e <= smallest or smallest == None:
                smallest = e
                current = index + i

        del array[current]
        array.insert(index, e)

        index +=1

        return selection_sort(array, index) # Recurse



# Test

nums = range(100)

shuffle(nums)

assert nums != sorted(nums)

assert selection_sort(nums) == sorted(nums)

