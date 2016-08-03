#!/usr/bin/evn python
# -*- coding: utf-8 -*-

import os
import unittest

from utils.read_data_file import read_int_array
from searching.binary_search import search
from sorting.quick_sort import sort


BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class BinarySearchTester(unittest.TestCase):

    def setUp(self):

        self.collection = read_int_array(os.path.join(BASE_DIR, 'data1.data'))
        self.collection = sort(self.collection)

    def test_search_exist(self):

        result = search(self.collection, 444)
        self.assertEqual(result, True)

    def test_search_not_exist(self):

        result = search(self.collection, -1)
        self.assertEqual(result, False)

    def test_search_empty_collection(self):

        self.collection = []
        result = search(self.collection, 444)
        self.assertEqual(result, False)


if __name__ == '__main__':

    unittest.main()
