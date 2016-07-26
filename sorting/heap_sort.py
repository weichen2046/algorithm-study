#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Heap Sort.

Best, Average, Worst: O(nlog(n)).
'''


def heapify(array, i, n, order):
    '''
    Recursively enforce that array[i, n) is a valid heap.
    '''

    left  = 2 * i + 1
    right = 2 * i + 2

    mark = i

    if order == 'asc':
        if left < n and array[left] > array[mark]:
            mark = left

        if right < n and array[right] > array[mark]:
            mark = right
    else:
        if left < n and array[left] < array[mark]:
            mark = left

        if right < n and array[right] < array[mark]:
            mark = right

    if mark != i:
        array[i], array[mark] = array[mark], array[i]
        heapify(array, mark, n, order)


def build_heap(array, n, order):

    for i in xrange(n/2 -1, -1, -1):
        heapify(array, i, n, order)


def sort(array, order='asc'):
    '''
    In-place sort array use heap sort algorithm in ascending or descending
    order.

    Return the sorted array.
    '''

    if not array:
        raise Exception('No elements to sort.')

    n = len(array)

    build_heap(array, n, order)

    for i in xrange(n-1, 0, -1):
        array[0], array[i] = array[i], array[0]
        heapify(array, 0, i, order)

    return array


if __name__ == '__main__':

    import random
    from argparse import ArgumentParser

    parser = ArgumentParser(description='Sort array use Heap Sort algorithm.')
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
