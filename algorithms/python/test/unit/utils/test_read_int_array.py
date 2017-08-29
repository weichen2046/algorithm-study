#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import unittest

from utils.read_data_file import read_int_array


BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class ReadIntArrayTester(unittest.TestCase):

    # Test canonical data file test.
    def test_read_int_array_1(self):

        expect = [140, 589, 647, 445, 417, 86, 969, 76, 65, 444, 567, 637, 702, 113, 864]
        array = read_int_array(os.path.join(BASE_DIR, 'data1.data'))
        self.assertEqual(expect, array)

    # Test data file which contains empty lines.
    def test_read_int_array_2(self):

        expect = [140, 589, 647, 445, 417, 86, 969, 76, 65, 444, 567, 637, 702, 113, 864]
        array = read_int_array(os.path.join(BASE_DIR, 'data2.data'))
        self.assertEqual(expect, array)

    # Test data file which is empty.
    def test_read_int_array_3(self):

        expect = []
        array = read_int_array(os.path.join(BASE_DIR, 'empty_file.data'))
        self.assertEqual(expect, array)

    # Test data file which not exist.
    def test_read_int_array_4(self):

        expect = []
        array = read_int_array(os.path.join(BASE_DIR, 'not_exist.data'))
        self.assertEqual(expect, array)


if __name__ == '__main__':

    unittest.main()
