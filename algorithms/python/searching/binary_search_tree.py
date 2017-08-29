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

    def in_order(self, order):
        if order == 'asc':
            start = self.left
            end = self.right
        else:
            start = self.right
            end = self.left

        if start:
            for n in start.in_order(order):
                yield n

        yield self.value

        if end:
            for n in end.in_order(order):
                yield n

    def _remove_from_parent(self, parent, value):
        if parent:
            return parent.remove(value)

        return None

    def remove(self, value):
        if value == self.value:
            if not self.left:
                return self.right

            child = self.left
            while child.right:
                child = child.right

            child_v = child.value
            self.left = self._remove_from_parent(self.left, child_v)
            self.value = child_v

        elif value < self.value:
            self.left = self._remove_from_parent(self.left, value)

        else:
            self.right = self._remove_from_parent(self.right, value)

        return self


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

    def in_order(self, order='asc'):
        if order not in ['asc', 'desc']:
            raise ValueError('parameter order should be "asc" or "desc"')

        if not self.root:
            return

        for n in self.root.in_order(order):
            yield n

    def remove(self, value):
        if self.root:
            self.root = self.root.remove(value)
