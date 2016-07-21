#!/usr/bin/evn python
# -*- coding: utf-8 -*-

import os
import unittest

from convex_hull.helper import read_points


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/unit/'


class ConvexHullHelperTester(unittest.TestCase):

    def test_read_points_comma(self):
        expect = [(10, 10), (1, 15)]
        points = read_points(BASE_DIR + 'points_1.data')

        self.assertEqual(expect, points)

    def test_read_points_space(self):
        expect = [(10, 10), (1, 15), (2, 3)]
        points = read_points(BASE_DIR + 'points_2.data')

        self.assertEqual(expect, points)

    def test_read_points_semicolon(self):
        expect = [(10, 10), (1, 15), (2, 3)]
        points = read_points(BASE_DIR + 'points_3.data')

        self.assertEqual(expect, points)


if __name__ == '__main__':

    unittest.main()
