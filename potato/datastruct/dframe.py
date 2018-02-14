import pandas
import logging
import numpy

logger = logging.getLogger(__name__)


class DFrame(object):

    """
        Streams chunks of data from the iterator in form of a pandas dataframe.
    """

    def __init__(self, frame, column_names, seperator=",", skip_title=True):
        self.frame = frame
        self.column_names = column_names
        self.skip_title = skip_title

        self.custom_maps = []

    def init_frame(self):
        self.frame.apply_map(lambda x: x.strip())
        self.frame.apply_map(lambda x: x.split(","))

    def add_custom_map(self, map_func):
        self.custom_maps.append(lambda x: map_func(x))

    def get_generator(self, batch_size=1000):

        """
            Returns generator which pulls out pandas dataframes of size batch_size from the frame.
        """

        if self.skip_title:
            _ = self.frame.take(1)

        self.init_frame()

        for _map in self.custom_maps:
            self.frame.apply_map(_map)

        def _generator():

            while 1:

                chunk = self.frame.take(batch_size)

                if len(chunk) == 0:
                    break

                yield pandas.DataFrame(chunk, columns=self.column_names)

        return _generator()
