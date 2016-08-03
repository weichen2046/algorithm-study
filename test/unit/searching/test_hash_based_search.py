#!/usr/bin/evn python
# -*- coding: utf-8 -*-

import os
import unittest

from utils.read_data_file import read_array
from searching.hash_based_search import search


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJ_DIR = os.path.dirname(os.path.dirname(os.path.dirname(BASE_DIR)))
RES_DIR = os.path.join(PROJ_DIR, 'res/data')
WORDS_FILE = os.path.join(RES_DIR, 'english_words.txt')


class HashBasedSearchTester(unittest.TestCase):

    def setUp(self):

        self.collection = read_array(WORDS_FILE, 100)

    def test_search_exist(self):

        result = search(self.collection, 'aaa')
        self.assertEqual(result, True)

        result = search(self.collection, 'abacterial')
        self.assertEqual(result, True)

        result = search(self.collection, 'abased')
        self.assertEqual(result, True)

    def test_search_not_exist(self):

        result = search(self.collection, '12345')
        self.assertEqual(result, False)

        result = search(self.collection, 'zythum')
        self.assertEqual(result, False)

        result = search(self.collection, 'zyzzyvas')
        self.assertEqual(result, False)

    def test_search_empty_collection(self):

        self.collection = []
        result = search(self.collection, 'aaa')
        self.assertEqual(result, False)


if __name__ == '__main__':

    unittest.main()
