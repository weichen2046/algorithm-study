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
