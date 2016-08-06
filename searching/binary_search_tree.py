#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Binary Search Tree.
A degenerate Binary Search Tree is just like a linked list and result in linear
search time.

Best: O(1), Average: O(logn), Worst: O(n)
'''


class BinaryNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def add(self, value):
        if value <= self.value:
            if not self.left:
                self.left = BinaryNode(value)
            else:
                self.left.add(value)
        else:
            if not self.right:
                self.right = BinaryNode(value)
            else:
                self.right.add(value)


class BinarySearchTree:

    def __init__(self):
        self.size = 0
        self.root = None

    def add(self, value):
        if not self.root:
            self.root = BinaryNode(value)
        else:
            self.root.add(value)
        self.size += 1

    def __len__(self):
        return self.size

    def __contains__(self, target):
        node = self.root
        while node:
            if target == node.value:
                return True
            elif target < node.value:
                node = node.left
            else:
                node = node.right
        return False
