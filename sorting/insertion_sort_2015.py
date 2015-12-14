#!/usr/bin/python2
# -*- coding: utf-8 -*-

from random import shuffle
 

li = range(1, 50)
shuffle(li)

for i in range(len(li)):
    while li[i] < li[i - 1] and i > 0: 
        li.insert(i-1, li[i])
        del li[i+1]
        i -= 1

assert li == sorted(li)


# With swapping: 

li = range(1, 1000)
shuffle(li)


for i in range(len(li)):
    while li[i] < li[i - 1] and i > 0:      
        li[i], li[i - 1] = li[i - 1], li[i] 
        i -= 1

assert li == sorted(li)