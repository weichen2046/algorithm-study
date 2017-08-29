#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Bucket Sort.

Best, Average, Worst: O(n).
'''

from insertion_sort import sort as insertion_sort


_HASH_DENOMINATOR = 100
_BUCKET_NUM = 10


def hash_elem(elem):

    return  elem / _HASH_DENOMINATOR


def get_bucket_num(elem_num):

    return _BUCKET_NUM


def extract(buckets, array, order):
    '''
    Copy elements from buckets back to array.
    '''

    if order == 'asc':
        i = 0
        d = 1
    else:
        i = len(array) - 1
        d = -1

    for bucket in buckets:
        if not bucket:
            continue

        if len(bucket) > 1:
            # sort bucket first
            insertion_sort(bucket)
            for b in bucket:
                array[i] = b
                i += d
        else:
            # bucket only has one element
            array[i] = bucket[0]
            i += d


def sort(array, order='asc', bucket_num_getter=None, hasher=None):
    '''
    Sort array use bucket sort algorithm in ascending or descending
    order. Use bucket sort when the following two properties hold:

    * Uniform distribution
      - The input data must uniformly distributed for a given range. Based on
        this distribution, n buckets are created to evently partition the input
        range.
    * Ordered hash function
      - The buckets are ordered. If i < j, elements inserted into bucket b(i)
        are lexicographically smaller than elements in bucket b(j).

    Reference: George T. Heineman, Gary Pollice and Stanley Selkow's Algorithms
    in a Nutshell, 2nd Edition

    Return the sorted array.
    '''

    if not array:
        raise Exception('No element to sort.')

    n = len(array)

    if not bucket_num_getter:
        bucket_num_getter = get_bucket_num

    if not hasher:
        hasher = hash_elem

    bucket_num = bucket_num_getter(n)

    # create buckets
    buckets = [None] * bucket_num

    for i in xrange(0, n):
        elem = array[i]
        k = hasher(elem)
        if not buckets[k]:
            buckets[k] = []
        buckets[k].append(elem)

    extract(buckets, array, order)

    return array


if __name__ == '__main__':

    import random
    from argparse import ArgumentParser

    parser = ArgumentParser(description='Sort array use Insertion Sort algorithm.')
    parser.add_argument('random', type=int, help='max random number count')
    parser.add_argument('--order', type=str, default='asc', choices=['asc', 'desc'],
            help='sort in ascending or descending.')

    args = parser.parse_args()

    _BUCKET_NUM = args.random

    # to avoid 'ValueError("sample larger than population")' when call
    # random.sample().
    r_end = 1000
    if args.random >= r_end:
        r_end = args.random + 10
        _BUCKET_NUM = r_end

    _HASH_DENOMINATOR = r_end / args.random

    randoms = random.sample(xrange(1, r_end), args.random)

    print 'before sort:\t', randoms
    sort(randoms, args.order)
    print 'after sort:\t', randoms
