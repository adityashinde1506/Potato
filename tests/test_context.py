import unittest
import sys
import logging

#logging.basicConfig(level=logging.DEBUG)
sys.path.append("/home/adityas/Projects/Potato")

from potato.backend import *
from potato import Context

class TestContext(unittest.TestCase):

    def setUp(self):
        self.path="/home/adityas/Projects"
        self.context=Context(self.path,["\w+.txt"])

    def test_context_creation(self):
        self.assertIsNotNone(self.context.get_streamer())
