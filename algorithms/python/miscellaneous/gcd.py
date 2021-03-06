#!/usr/bin/env python
# -*- coding: utf-8 -*-


def gcd(a, b):
    '''
    Calculate the greatest common divisor use Euclid's gcd algorithm.

    Ref: http://www.cut-the-knot.org/blue/Euclid.shtml
    '''

    if a == 0 or b == 0:
        return 0

    while(b != 0):
        if a > b:
            a -= b
        else:
            b -= a

    return a


def mod_gcd(a, b):
    '''
    Calculate the greatest common divisor use the modulo operator.
    '''

    if a == b:
        return a

    if a == 0 or b == 0:
        return 0

    if a < b:
        a, b = b, a

    while(b != 0):
        r = a % b
        a = b
        b = r

    return a


if __name__ == '__main__':

    from argparse import ArgumentParser

    parser = ArgumentParser(description='Calculate the greatest common divisor.')
    parser.add_argument('a', type=int, help='argument 1, type integer.')
    parser.add_argument('b', type=int, help='argument 2, type integer.')
    parser.add_argument('--mod', action='store_true', help='use modulo operator to calc gcd.')

    args = parser.parse_args()

    if args.mod:
        print mod_gcd(args.a, args.b)
    else:
        print gcd(args.a, args.b)

    # Use the following line to get the elapsed time.
    #python -m timeit -s "from gcd import gcd" -n 1 -r 1 "gcd(1000000, 8)"
