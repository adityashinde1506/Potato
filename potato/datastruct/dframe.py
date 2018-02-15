import pandas
import logging
import numpy
from potato.datastruct.frame import Frame

logger = logging.getLogger(__name__)


class DFrame(Frame):

    """
        Streams chunks of data from the iterator in form of a pandas dataframe.
    """

    def __init__(self, streamer, column_names, seperator=",", skip_title=True):
        Frame.__init__(self, streamer)
        self.custom_maps = []
        self.column_names = column_names
        self.skip_title = skip_title

    def init_frame(self):
        self.apply_map(lambda x: x.strip())
        self.apply_map(lambda x: x.split(","))

    def add_custom_map(self, map_func):
        self.custom_maps.append(lambda x: map_func(x))

    def get_generator(self, batch_size=1000):

        """
            Returns generator which pulls out pandas dataframes of size batch_size from the frame.
        """

        if self.skip_title:
            _ = self.take(1)

        self.init_frame()

        for _map in self.custom_maps:
            self.apply_map(_map)

        def _generator():

            while 1:

                chunk = self.take(batch_size)

                if len(chunk) == 0:
                    break

                yield pandas.DataFrame(chunk, columns=self.column_names)

        return _generator()
