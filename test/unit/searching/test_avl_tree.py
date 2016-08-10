#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import random
import unittest

from searching.avl_tree import AVLTree
from utils.read_data_file import read_int_array


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJ_DIR = os.path.dirname(os.path.dirname(os.path.dirname(BASE_DIR)))
RES_DIR = os.path.join(PROJ_DIR, 'res/data')
DATA_FILE = os.path.join(RES_DIR, 'fifteen_unordered_ints.txt')


class AVLTreeTester(unittest.TestCase):

    def setUp(self):
        self.bst = AVLTree()

    def test_add(self):

        nums = random.sample(xrange(0, 1000), 100)
        for v in nums:
            self.bst.add(v)

        self.assertEqual(len(self.bst), 100)

    def test_contains(self):
        nums = random.sample(xrange(0, 1000), 100)
        exist = nums[0]
        fake = 1800

        for v in nums:
            self.bst.add(v)

        self.assertEqual(exist in self.bst, True)
        self.assertEqual(fake in self.bst, False)

    def test_in_order(self):
        nums = read_int_array(DATA_FILE)
        for v in nums:
            self.bst.add(v)

        ordered = [n for n in self.bst.in_order()]
        expect = [65, 76, 86, 113, 140, 417, 444, 445, 567, 589, 637, 647, 702, 864, 969]
        self.assertEqual(ordered, expect)

    def test_in_order_in_reverse(self):
        nums = read_int_array(DATA_FILE)
        for v in nums:
            self.bst.add(v)

        ordered = [n for n in self.bst.in_order('desc')]
        expect = [969, 864, 702, 647, 637, 589, 567, 445, 444, 417, 140, 113, 86, 76, 65]
        self.assertEqual(ordered, expect)

    def test_in_order_with_empty_bst(self):
        ordered = [n for n in self.bst.in_order()]
        self.assertEqual(ordered, [])

    def test_in_order_with_error_order_param(self):
        with self.assertRaises(ValueError):
            ordered = [n for n in self.bst.in_order('test')]
            self.assertEqual(ordered, [])


if __name__ == '__main__':

    unittest.main()
