#!/usr/bin/evn python
# -*- coding: utf-8 -*-

'''
Helper function for read data from file.
'''


def read_array(f_name, max=None):
    '''
    Read data in the file named f_name. Each line of the input file contains
    one element.

    Return a string array, max length of the array defined by parameter max. If
    max is None, then return all read elements.
    '''

    count = 0
    array = []
    try:
        with open(f_name) as f:
            line = f.readline()
            while(line):
                if max and count >= max:
                    break

                line = line.strip()
                if line:
                    count += 1
                    array.append(line)

                line = f.readline()
    except IOError:
        pass

    return array


def read_int_array(f_name, max=None):
    '''
    Read data in the file named f_name. Each line of the input file contains
    one number.

    Return an int array, max length of the array defined by parameter max. If
    max is None, then return all read integers.    '''

    array = read_array(f_name, max)

    return [ int(e) for e in array ]


def read_points(f_name):
    '''
    Read points data from file.

    Return an array of tuples that represents the points in Cartesian
    coordinate system.
    '''

    points = []
    try:
        import re
        prog = re.compile(' |;|,')
        with open(f_name) as f:
            line = f.readline()
            while(line):
                p = tuple([ int(c) for c in prog.split(line.strip()) if c])
                if p:
                    points.append(p)
                line = f.readline()
    except IOError as e:
        print e

    return points
