import unittest
import sys
import logging
import time

logging.basicConfig(level=logging.DEBUG)
sys.path.append("/home/adityas/Projects/Potato")

from potato.context import Context
from potato.datastruct.dframe import DFrame


def dtype_converter(row):

    dtypes = [str, float]

    for i in range(len(row)):
        row[i] = dtypes[i](row[i])

    return row


class TestDFrame(unittest.TestCase):

    def setUp(self):
        self.context = Context("/home/adityas/Kaggle/NAB", ["art_daily_no_noise.csv"])

        #self.frame = self.context.get_frame()
        self.dframe = self.context.get_dframe(["time", "val"])
#       self.dframe.add_custom_map(dtype_converter)

    def test_generator_run(self):
        gen = self.dframe.get_generator()

        for data in gen:
            print(data.shape)

    def test_streamer(self):
        s = self.dframe.streamer
        while 1:
            line = s.get_single_line()
            if not line:
                break

        #print(len(self.frame.collect()))


if __name__ == "__main__":
    unittest.main()
