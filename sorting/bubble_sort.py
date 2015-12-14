#!/usr/bin/python2
# -*- coding: utf-8 -*-

'''
Bubble sort: Starting from the beginning of the list, compare every adjacent pair, swap their position if they are not in the right order (the latter one is smaller than the former one). After each iteration, one less element (the last one) is needed to be compared until there are no more elements left to be compared. (Wiktionary)
'''


from random import shuffle

li = range(1, 1000)
shuffle(li)

for x in range(len(li)-1, 0 - 1, -1):
	for i in range(x):
		if li[i] > li[i+1]:
			li[i], li[i+1] = li[i+1], li[i]


assert li == sorted(li)
