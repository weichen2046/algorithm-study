#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from searching.bloom_filter import BloomFilter


class BloomFilterTester(unittest.TestCase):

    def setUp(self):
        self.bf = BloomFilter(size=1000)

    def test_contains(self):
        self.bf.add(456)
        self.assertEqual(234 in self.bf, False)

    def test_add(self):
        for e in xrange(0, 500):
            self.bf.add(e)

        for e in xrange(500, 1000):
            self.assertEqual(e in self.bf, False)


if __name__ == '__main__':

    unittest.main()
