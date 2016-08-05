#!/usr/bin/evn python
# -*- coding: utf-8 -*-

'''
Bloom Filter.
A Bloom Filter demonstrates efficient memory usage but it is only useful when
false positive can be tolerated. E.g. using a Bloom Filter to confirm whether
to conduct an expensive search over disk-based storage.

Best, Average, Worst: O(k)
'''


class BloomFilter:

    def __init__(self, size=1000, hash_funcs=None):
        self.bits = 0
        self.size = size

        if not hash_funcs:
            self.k = 1
            self.hash_funcs = [lambda e, size: hash(e) % size]
        else:
            self.k = len(hash_funcs)
            self.hash_funcs = hash_funcs

    def add(self, e):
        for hf in self.hash_funcs:
            self.bits |= 1 << hf(e, self.size)

    def __contains__(self, target):
        '''
        A false positive might be returned even if the `target` is not present.
        However, a false negative will never be returned.

        Return `False` if target not present, return `True` means target might
        added to set.
        '''

        for hf in self.hash_funcs:
            if self.bits & (1 << hf(target, self.size)) == 0:
                return False

        return True
