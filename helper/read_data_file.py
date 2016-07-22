#!/usr/bin/evn python
# -*- coding: utf-8 -*-

'''
Helper function for read data from file.
'''


def read_int_array(f_name):
    '''
    Read data in the file named f_name. Each line of the input file contains
    one number.

    Return an int array.
    '''

    array = []
    try:
        with open(f_name) as f:
            line = f.readline()
            while(line):
                line = line.strip()
                if line:
                    array.append(int(line))
                line = f.readline()
    except IOError:
        pass

    return array


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
