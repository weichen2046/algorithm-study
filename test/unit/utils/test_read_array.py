#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import unittest

from utils.read_data_file import read_array


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJ_DIR = os.path.dirname(os.path.dirname(os.path.dirname(BASE_DIR)))
RES_DIR = os.path.join(PROJ_DIR, 'res/data')
WORDS_FILE = os.path.join(RES_DIR, 'english_words.txt')


class ReadArrayTester(unittest.TestCase):

    def test_read_array_1(self):

        words = read_array(WORDS_FILE, 10)

        self.assertEqual(10, len(words))

        expect = ['a', 'aa', 'aaa', 'aah', 'aahed', 'aahing', 'aahs', 'aal',
                'aalii', 'aaliis']

        self.assertEqual(words, expect)

    def test_read_array_2(self):

        words = read_array(WORDS_FILE)

        try:
            import subprocess32 as subprocess
        except ImportError:
            import subprocess

        output = subprocess.check_output(['cat %s | wc -l' % WORDS_FILE],
                shell=True)
        expect = int(output.strip())

        self.assertEqual(expect, len(words))
