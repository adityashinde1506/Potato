import unittest
import sys
import logging

logging.basicConfig(level=logging.DEBUG)
sys.path.append("/home/adityas/Projects/Potato")

from potato.context import Context
from potato.datastruct.dframe import DFrame


class TestDFrame(unittest.TestCase):

    def setUp(self):
        self.context = Context("/home/adityas/Kaggle/NAB", ["art_daily_no_noise.csv"])

        self.frame = self.context.get_frame()
        self.dframe = DFrame(self.frame, ["time", "val"])

    def test_generator_run(self):
        gen = self.dframe.get_generator()
        while 1:
            print(next(gen))
            break


if __name__ == "__main__":
    unittest.main()
