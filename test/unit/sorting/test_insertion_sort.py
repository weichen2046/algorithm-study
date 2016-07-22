#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import unittest

from helper.read_data_file import read_int_array
from sorting.insertion_sort import sort


BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class InsertionSortTester(unittest.TestCase):

    def test_sort_default(self):
        '''
        Test sort in default order, i.e., in ascending order.
        '''

        array = read_int_array(os.path.join(BASE_DIR, 'data1.data'))
        array = sort(array)
        expect = [65, 76, 86, 113, 140, 417, 444, 445, 567, 589, 637, 647, 702, 864, 969]
        self.assertEqual(expect, array)

    def test_sort_ascending(self):
        '''
        Test sort in ascending order.
        '''

        array = read_int_array(os.path.join(BASE_DIR, 'data1.data'))
        array = sort(array, 'asc')
        expect = [65, 76, 86, 113, 140, 417, 444, 445, 567, 589, 637, 647, 702, 864, 969]
        self.assertEqual(expect, array)

    def test_sort_descending(self):
        '''
        Test sort in descending order.
        '''

        array = read_int_array(os.path.join(BASE_DIR, 'data1.data'))
        array = sort(array, 'desc')
        expect = [969, 864, 702, 647, 637, 589, 567, 445, 444, 417, 140, 113, 86, 76, 65]
        self.assertEqual(expect, array)
