#!/usr/bin/python2
# -*- coding: utf-8 -*-

import os


def breadth_first(siblings=[], generations=[]):
    '''
    Perform a breadth-first search / walkthrough on a directory 
    (containing only directories, no files).
    '''	
    if siblings == []:
        return generations 
    else:
        generations.append([i[-1] for i in siblings])	

        children = []
        for sibling in siblings:
            children.extend(sibling+'/'+i for i in os.listdir(sibling))

        return breadth_first(children, generations=generations)


# Test 

r = '/testroot/'

print breadth_first(siblings=[r])
