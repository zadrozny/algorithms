#!/usr/bin/python
# -*- coding: utf-8 -*-


'''
You have 2d integer array where 1's signify land and 0's signify water.

Find the number of "islands" in the array, 
where an island is defined as a continuous block of 1's.

1's are continuous if they are adjacent via a left, right, up, or down move, 
but not diagonal (water flows over the diagonals)
'''

m = [[0, 0, 1],
     [0, 1, 0], 
     [0, 0, 1]]

islands = 0

for y in range(len(m)):
    for x in range(len(m[0])):
        if m[y][x] == 1:

            if x > 0:               # Look left 
                if m[y][x-1] == 1:
                    continue
            
            if y > 0:               # Look up
                if m[y-1][x] == 1:
                    continue

            islands += 1

print islands                