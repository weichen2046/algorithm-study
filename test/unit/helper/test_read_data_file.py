#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import unittest

from helper.read_data_file import read_int_array


BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class ReadDataFileTester(unittest.TestCase):

    def test_read_int_array_1(self):
        '''
        Test canonical data file test.
        '''

        expect = [140, 589, 647, 445, 417, 86, 969, 76, 65, 444, 567, 637, 702, 113, 864]
        array = read_int_array(os.path.join(BASE_DIR, 'data1.data'))
        self.assertEqual(expect, array)

    def test_read_int_array_2(self):
        '''
        Test data file which contains empty lines.
        '''

        expect = [140, 589, 647, 445, 417, 86, 969, 76, 65, 444, 567, 637, 702, 113, 864]
        array = read_int_array(os.path.join(BASE_DIR, 'data2.data'))
        self.assertEqual(expect, array)

    def test_read_int_array_3(self):
        '''
        Test data file which is empty.
        '''

        expect = []
        array = read_int_array(os.path.join(BASE_DIR, 'data3.data'))
        self.assertEqual(expect, array)

    def test_read_int_array_4(self):
        '''
        Test data file which not exist.
        '''

        expect = []
        array = read_int_array(os.path.join(BASE_DIR, 'not_exist.data'))
        self.assertEqual(expect, array)

    


if __name__ == '__main__':

    unittest.main()
