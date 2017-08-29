#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
A well-known sort algorithm, called Selection Sort. It is an application of
greedy strategy.
'''


def sort(array, order='asc'):
    '''
    Greedy approach to sort an array in ascending or descending order.
    This sort algorithm also known as Selection Sort.
    '''

    if not array:
        raise Exception('No elements to sort.')

    l = len(array)
    for i in xrange(l - 1):
        m = i
        for j in xrange(i+1, l):
            if order == 'asc':
                if array[j] < array[m]:
                    m = j
            else:
                if array[j] > array[m]:
                    m = j

        if m != i:
            array[m], array[i] = array[i], array[m]


if __name__ == '__main__':

    import random
    from argparse import ArgumentParser
    
    parser = ArgumentParser(description='Sort array use Selection Sort algorithm.')
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
