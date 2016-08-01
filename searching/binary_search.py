#!/usr/bin/evn python
# -*- coding: utf-8 -*-

'''
Binary Search.

Best: O(1), Average, Worst: O(logn)
'''


def search(c, t):
    '''
    Search target t in collection c.

    Note: collection c must be soreted already in ascending order.

    Return True if t in c, otherwise return False.
    '''

    if not c:
        return False

    low = 0
    high = len(c) - 1
    while (low <= high):
        mid = (low + high) // 2
        if t < c[mid]:
            high = mid - 1
        elif t > c[mid]:
            low = mid + 1
        else:
            return True

    return False
