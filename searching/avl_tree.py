#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
AVL Tree.

Best: O(1), Average, Worst: O(logn)
'''


class BinaryNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 0

    def _calc_height(self):
        height = -1

        if self.left:
            height = max(height, self.left.height)

        if self.right:
            height = max(height, self.right.height)

        self.height = height + 1

    def _height_difference(self):
        left_h = -1 if not self.left else self.left.height
        right_h = -1 if not self.right else self.right.height

        return left_h - right_h

    def _add_to_parent(self, parent, value):
        if not parent:
            return BinaryNode(value)

        return parent.add(value)

    def _rotate_right(self):
        new_root = self.left
        self.left = new_root.right
        new_root.right = self
        self._calc_height()
        return new_root

    def _rotate_left(self):
        new_root = self.right
        self.right = new_root.left
        new_root.left = self
        self._calc_height()
        return new_root

    def _rotate_right_left(self):
        new_root = self.right.left
        child = self.right
        child.left = new_root.right
        self.right = new_root.left
        new_root.left = self
        new_root.right = child
        child._calc_height()
        self._calc_height()
        return new_root

    def _rotate_left_right(self):
        new_root = self.left.right
        child = self.left
        child.right = new_root.left
        self.left = new_root.right
        new_root.left = child
        new_root.right = self
        child._calc_height()
        self._calc_height()
        return new_root

    def add(self, value):
        new_root = self

        if value <= self.value:
            self.left = self._add_to_parent(self.left, value)
            if self._height_difference() == 2:
                if value <= self.left.value:
                    new_root = self._rotate_right()

                else:
                    new_root = self._rotate_left_right()

        else:
            self.right = self._add_to_parent(self.right, value)
            if self._height_difference() == -2:
                if value <= self.right.value:
                    new_root = self._rotate_right_left()

                else:
                    new_root = self._rotate_left()

        new_root._calc_height()
        return new_root

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


class AVLTree:

    def __init__(self):
        self.size = 0
        self.root = None

    def add(self, value):
        if not self.root:
            self.root = BinaryNode(value)
        else:
            self.root = self.root.add(value)
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
