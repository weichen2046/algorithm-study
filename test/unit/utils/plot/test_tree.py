#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import unittest

from searching.binary_search_tree import BinarySearchTree
from searching.avl_tree import AVLTree
from utils.plot.tree import get_edges, plot
from utils.read_data_file import read_int_array


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJ_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(BASE_DIR))))
RES_DIR = os.path.join(PROJ_DIR, 'res/data')
DATA_FILE = os.path.join(RES_DIR, 'fifteen_unordered_ints.txt')


class TreePlotterTester(unittest.TestCase):

    def test_get_edges(self):

        bst = BinarySearchTree()
        bst.add(10)
        bst.add(2)
        bst.add(12)
        bst.add(14)
        bst.add(1)

        edges = get_edges(bst)
        expect = [(2, 1), (10, 2), (10, 12), (12, 14)]

        self.assertItemsEqual(expect, edges)

    def test_plot(self):

        avl = AVLTree()
        nums = read_int_array(DATA_FILE)
        for v in nums:
            avl.add(v)

        plot(avl)

        # check file tree_graph.png exist
        graph_file = 'tree_graph.png'
        is_file = os.path.isfile(graph_file)

        if is_file:
            os.remove(graph_file)

        self.assertEqual(is_file, True)


if __name__ == '__main__':

    unittest.main()
