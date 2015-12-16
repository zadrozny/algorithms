#!/usr/bin/python2
# -*- coding: utf-8 -*-

import os



def depth_first(children=None, stack=[]):
	'''
	Perform a depth-first search / walkthrough on a directory (containing only directories, no files). The first 
	'''

	children = [children + '/' + c for c in os.listdir(children)]

	for c in children:
		stack.append(c)
		depth_first(children=c, stack=stack)

	return stack



r = '/'
print '\n'.join(depth_first(children=r))