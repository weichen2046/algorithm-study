#!/usr/bin/evn python
# -*- coding: utf-8 -*-

'''
Helper functions.
'''


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
