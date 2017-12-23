import unittest
import sys
import logging

#logging.basicConfig(level=logging.DEBUG)
sys.path.append("/home/adityas/Projects/Potato")

from potato.streamer import Streamer
from potato.search_utils import get_data_files

class TestStreamer(unittest.TestCase):

    def setUp(self):
        self.path="/home/adityas/Projects/Experiment_Results"
        self.files=get_data_files(self.path,["ztomatrix.txt"])
        
    def test_single_line_getter(self):
        streamer=Streamer(self.files)
        for i in range(5):
            print(streamer.get_single_line())

