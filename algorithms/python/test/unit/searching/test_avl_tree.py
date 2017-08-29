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
        self.avl = AVLTree()

    def test_add(self):

        nums = random.sample(xrange(0, 1000), 100)
        for v in nums:
            self.avl.add(v)

        self.assertEqual(len(self.avl), 100)

    def test_contains(self):
        nums = random.sample(xrange(0, 1000), 100)
        exist = nums[0]
        fake = 1800

        for v in nums:
            self.avl.add(v)

        self.assertEqual(exist in self.avl, True)
        self.assertEqual(fake in self.avl, False)

    def test_in_order(self):
        nums = read_int_array(DATA_FILE)
        for v in nums:
            self.avl.add(v)

        ordered = [n for n in self.avl.in_order()]
        expect = [65, 76, 86, 113, 140, 417, 444, 445, 567, 589, 637, 647, 702, 864, 969]
        self.assertEqual(ordered, expect)

    def test_in_order_in_reverse(self):
        nums = read_int_array(DATA_FILE)
        for v in nums:
            self.avl.add(v)

        ordered = [n for n in self.avl.in_order('desc')]
        expect = [969, 864, 702, 647, 637, 589, 567, 445, 444, 417, 140, 113, 86, 76, 65]
        self.assertEqual(ordered, expect)

    def test_in_order_with_empty_avl(self):
        ordered = [n for n in self.avl.in_order()]
        self.assertEqual(ordered, [])

    def test_in_order_with_error_order_param(self):
        with self.assertRaises(ValueError):
            ordered = [n for n in self.avl.in_order('test')]
            self.assertEqual(ordered, [])

    def test_remove(self):
        nums = read_int_array(DATA_FILE)
        for v in nums:
            self.avl.add(v)

        self.avl.remove(76)
        ordered = [n for n in self.avl.in_order()]
        expect = [65, 86, 113, 140, 417, 444, 445, 567, 589, 637, 647, 702, 864, 969]
        self.assertEqual(ordered, expect)

        self.avl.remove(65)
        ordered = [n for n in self.avl.in_order()]
        expect = [86, 113, 140, 417, 444, 445, 567, 589, 637, 647, 702, 864, 969]
        self.assertEqual(ordered, expect)

        self.avl.remove(969)
        ordered = [n for n in self.avl.in_order()]
        expect = [86, 113, 140, 417, 444, 445, 567, 589, 637, 647, 702, 864]
        self.assertEqual(ordered, expect)

        self.avl.remove(702)
        ordered = [n for n in self.avl.in_order()]
        expect = [86, 113, 140, 417, 444, 445, 567, 589, 637, 647, 864]
        self.assertEqual(ordered, expect)

        self.avl.remove(417)
        self.avl.remove(567)
        self.avl.remove(445)
        self.avl.remove(444)
        ordered = [n for n in self.avl.in_order()]
        expect = [86, 113, 140, 589, 637, 647, 864]
        self.assertEqual(ordered, expect)


if __name__ == '__main__':

    unittest.main()
