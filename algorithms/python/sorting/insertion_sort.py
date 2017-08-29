#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Insertion Sort.

Best: O(n) Average, Worst: O(n^2).
'''


def _insert_helper(array, pos, value, order):

    i = pos - 1

    if order == 'asc':
        left = array[i]
        right = value
    else:
        left = value
        right = array[i]

    while(i >= 0 and left > right):
        array[i+1] = array[i]
        i -= 1

        if order == 'asc':
            left = array[i]
        else:
            right = array[i]

    if pos != (i+1):
        array[i+1] = value


def sort(array, order='asc'):
    '''
    In-place sort array use insertion sort algorithm in ascending or descending
    order. In the following circumstances you shoud consider this approach:

    * Only a few items to sort.
    * Items are mostely sorted already.
    * Desire to write as little code as possible.

    Return the sorted array.
    '''

    if not array:
        raise Exception('No element to sort.')

    l = len(array)

    for i in range(1, l):
        _insert_helper(array, i, array[i], order)

    return array


if __name__ == '__main__':

    import random
    from argparse import ArgumentParser

    parser = ArgumentParser(description='Sort array use Insertion Sort algorithm.')
    parser.add_argument('random', type=int, help='max random number count')
    parser.add_argument('--order', type=str, default='asc', choices=['asc', 'desc'],
            help='sort in ascending or descending.')

    args = parser.parse_args()

    # to avoid 'ValueError("sample larger than population")' when call
    # random.sample().
    r_end = 1000
    if args.random >= r_end:
        r_end = args.random + 10

    randoms = random.sample(xrange(1, r_end), args.random)

    print 'before sort:\t', randoms
    sort(randoms, args.order)
    print 'after sort:\t', randoms
