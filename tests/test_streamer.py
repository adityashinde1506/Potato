import unittest
import sys
import logging

#logging.basicConfig(level=logging.DEBUG)
sys.path.append("/home/adityas/Projects/Potato")

from potato.backend import *

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

    def test_chunk_getter(self):
        streamer=Streamer(self.files)
        chunk=streamer.get_chunk(1000)
        self.assertEqual(len(chunk),1000)

    def test_insane_chunk_getter(self):
        streamer=Streamer(self.files)
        chunk=streamer.get_chunk(1000000000)
        self.assertNotEqual(len(chunk),1000000000)

    def test_generator_run(self):
        streamer=Streamer(self.files)
        generator=streamer.get_generator()
        i=0
        for line in generator:
            pass
