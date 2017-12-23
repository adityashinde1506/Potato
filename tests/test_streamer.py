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
        lines=[]
        for i in range(5):
            lines.append(streamer.get_single_line())
        self.assertEqual(len(lines),5)


    def test_file_change(self):
        streamer=Streamer(self.files)
        lines=[]
        for i in range(10000):
            lines.append(streamer.get_single_line())
        lines=list(filter(lambda x:x!=None,lines))
        self.assertEqual(len(lines),10000)

    def test_iterator_end(self):
        streamer=Streamer(self.files)
        for i in range(1000000):
            line=streamer.get_single_line()
        self.assertIsNone(line)
