#!/usr/bin/evn python
# -*- coding: utf-8 -*-

'''
Sequential Search.

Best: O(1), Average, Worst: O(n)
'''


def search(c, t):
    '''
    Search target t in collection c.

    Return True if t in c, otherwise return False.
    '''

    if not c:
        return False

    for e in c:
        if e == t:
            return True

    return False
