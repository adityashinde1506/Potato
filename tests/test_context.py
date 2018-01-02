import unittest
import sys
import logging

#logging.basicConfig(level=logging.DEBUG)
sys.path.append("/home/adityas/Projects/Potato")

from potato.backend import *
from potato.context import *

class TestContext(unittest.TestCase):

    def setUp(self):
        self.path="/home/adityas/Projects/Experiment_Results"
        self.context=Context(self.path,["ztomatrix.txt"])

    def test_context_creation(self):
        self.assertIsNotNone(self.context.get_streamer())