#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Use divide and conquer strategy to finding maximum element in array.
'''


def _max_elem(array, left, right):
    '''
    Compute the maximum element in subproblem array[left, right).

    Note: right end element is not part of the range.
    '''

    if (right - left) == 1:
        return array[left]

    mid = (left + right) / 2
    max1 = _max_elem(array, left, mid)
    max2 = _max_elem(array, mid, right)

    return max(max1, max2)


def max_elem(array):
    '''
    Use recursive divide and conquer approach to finding the maximum element in
    the given array.

    Return the maximum element.
    '''

    if not array:
        raise Exception('No element to operate.')

    return _max_elem(array, 0, len(array))


if __name__ == '__main__':

    import random
    from argparse import ArgumentParser

    parser = ArgumentParser(description='Get the maximum number.')
    parser.add_argument('random', type=int, help='max random number count.')

    args = parser.parse_args()

    # to avoid 'ValueError("sample larger than population")' when call
    # random.sample().
    r_end = 1000
    if args.random >= r_end:
        r_end = args.random + 10

    # generate random numbers
    randoms = random.sample(xrange(1, r_end), args.random)

    print 'array:\t', randoms
    print 'max:\t', max_elem(randoms)
