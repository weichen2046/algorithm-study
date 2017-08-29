#!/usr/bin/evn python
# -*- coding: utf-8 -*-

'''
Hash based Search.

Best, Average: O(1) Worst: O(n)
'''


def hash_fun(e, size):
    '''
    Default sample hash function.
    '''

    return hash(e) % size


def load_hash_table(c, size, hash_method):
    '''
    Hash elements in collection <c> to hash table bins with size of <size>.
    '''

    table = [None] * size

    for e in c:
        h = hash_method(e, size)
        if not table[h]:
            table[h] = []

        table[h].append(e)

    return table


def search(c, t, hash_method=None):
    '''
    Search target t in collection c.

    Return True if t in c, otherwise return False.
    '''

    if not c:
        return False

    n = len(c)

    if not hash_method:
        hash_method = hash_fun

    table = load_hash_table(c, n, hash_method)

    h = hash_method(t, n)

    if table[h]:
        return t in table[h]

    return False
