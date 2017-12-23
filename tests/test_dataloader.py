import unittest
import sys
import logging

#logging.basicConfig(level=logging.DEBUG)
sys.path.append("/home/adityas/Projects/Potato")

from potato.search_utils import *

class TestDirLoader(unittest.TestCase):

    def setUp(self):
        self.path="/home/adityas/Projects/Experiment_Results"

    def test_file_getter(self):
        files=get_data_files(self.path,["ztomatrix.txt"])
        self.assertIsNotNone(files)
        print(files)
        

