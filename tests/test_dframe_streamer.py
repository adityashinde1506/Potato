import unittest
import sys
import logging
import time

logging.basicConfig(level=logging.DEBUG)
sys.path.append("/home/adityas/Projects/Potato")

from potato.backend.search_utils import get_data_files
from potato.backend import DFStreamer


class TestDFrameStreamer(unittest.TestCase):

    def setUp(self):
        self.data_files = get_data_files("/home/adityas/Kaggle/SensorWeb/data", ["\S+.csv"])

    def test_streamer(self):
        dfstreamer = DFStreamer(self.data_files)
        df_gen = dfstreamer.get_generator()

        for batch in df_gen:
            print(batch.shape)


if __name__ == "__main__":
    unittest.main()
