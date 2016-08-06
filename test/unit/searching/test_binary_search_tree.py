#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import unittest

from searching.binary_search_tree import BinarySearchTree


class BinarySearchTreeTester(unittest.TestCase):

    def setUp(self):
        self.bst = BinarySearchTree()

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


if __name__ == '__main__':

    unittest.main()
