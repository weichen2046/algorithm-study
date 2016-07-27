#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Quick Sort. It is an application of divide and conquer strategy.

Best, Average: O(nlogn), Worst: O(n^2).
'''


def partion(array, left, right, pivot, order):

    p = left
    pv = array[pivot]

    array[right], array[pivot] = array[pivot], array[right]

    if order == 'asc':
        for i in xrange(left, right):
            if array[i] <= pv:
                if i != p:
                    array[i], array[p] = array[p], array[i]
                p += 1
    else:
        for i in xrange(left, right):
            if array[i] >= pv:
                if i != p:
                    array[i], array[p] = array[p], array[i]
                p += 1

    array[p], array[right] = array[right], array[p]

    return p


def quick_sort(array, left, right, order):

    if left >= right:
        return

    # here we always use the middle index between left and right as the pivot,
    # it is not always the best one of course.
    pivot = left + (right - left) / 2

    p = partion(array, left, right, pivot, order)

    quick_sort(array, left, p - 1, order)
    quick_sort(array, p + 1, right, order)

    return array


def sort(array, order='asc'):
    '''
    In-place sort array use quick sort algorithm in ascending or descending
    order.

    Return the sorted array.
    '''

    if not array:
        raise Exception('No element to sort.')

    n = len(array)

    return quick_sort(array, 0, n - 1, order)


if __name__ == '__main__':

    import random
    from argparse import ArgumentParser

    parser = ArgumentParser(description='Sort array use Quick Sort algorithm.')
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
