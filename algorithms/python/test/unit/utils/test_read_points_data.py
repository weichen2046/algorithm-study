#!/usr/bin/evn python
# -*- coding: utf-8 -*-

import os
import unittest

from utils.read_data_file import read_points


BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class ReadPointsDataTester(unittest.TestCase):

    # Test posints data separate by comma.
    def test_read_points_comma(self):

        expect = [(10, 10), (1, 15)]
        points = read_points(os.path.join(BASE_DIR, 'points_1.data'))

        self.assertEqual(expect, points)

    # Test posints data separate by space.
    def test_read_points_space(self):

        expect = [(10, 10), (1, 15), (2, 3)]
        points = read_points(os.path.join(BASE_DIR, 'points_2.data'))

        self.assertEqual(expect, points)

    # Test posints data separate by semicolon.
    def test_read_points_semicolon(self):

        expect = [(10, 10), (1, 15), (2, 3)]
        points = read_points(os.path.join(BASE_DIR, 'points_3.data'))

        self.assertEqual(expect, points)


if __name__ == '__main__':

    unittest.main()
