#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Merge Sort.

Best, Average, Worst: O(nlogn).
'''


def merge_sort(array, result, left, right, order):

    if right - left < 2:
        return

    if (right - left) == 2:
        if order == 'asc':
            if result[left] > result[right-1]:
                result[left], result[right-1] = result[right-1], result[left]
        else:
            if result[left] < result[right-1]:
                result[left], result[right-1] = result[right-1], result[left]
        return

    mid = (right + left + 1) / 2
    merge_sort(result, array, left, mid, order)
    merge_sort(result, array, mid, right, order)

    i = left
    j = mid
    if order == 'asc':
        for x in xrange(left, right):
            if i >= mid or (j < right and array[i] > array[j]):
                result[x] = array[j]
                j += 1
            else:
                result[x] = array[i]
                i += 1
    else:
        for x in xrange(left, right):
            if i >= mid or (j < right and array[i] < array[j]):
                result[x] = array[j]
                j += 1
            else:
                result[x] = array[i]
                i += 1


def sort(array, order='asc'):
    '''
    In-place sort array use merge sort algorithm in ascending or descending
    order.

    Return the sorted array.
    '''

    if not array:
        raise Exception('No element to sort.')

    copy = list(array)

    merge_sort(copy, array, 0, len(array), order)

    return array


if __name__ == '__main__':

    import random
    from argparse import ArgumentParser

    parser = ArgumentParser(description='Sort array use Merge Sort algorithm.')
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
