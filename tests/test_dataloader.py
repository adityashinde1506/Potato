import unittest
import sys
import logging

#logging.basicConfig(level=logging.DEBUG)
sys.path.append("/home/adityas/Projects/Potato")

from potato.backend import *

class TestDirLoader(unittest.TestCase):

    def setUp(self):
        self.path="/home/adityas/Projects"

    def test_file_getter(self):
        files=get_data_files(self.path,["\w+.txt"])
        self.assertIsNotNone(files)

    def test_regex(self):
        files=get_data_files(self.path,["\w+.txt"])
        rfiles=get_data_files(self.path,[r"\S*\.txt"])
        self.assertTrue(len(rfiles)>len(files))
