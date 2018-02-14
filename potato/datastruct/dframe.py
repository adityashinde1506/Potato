import pandas
import logging

logger = logging.getLogger(__name__)


class DFrame(object):

    """
        Streams chunks of data from the iterator in form of a pandas dataframe.
    """

    def __init__(self, frame, column_names, seperator=","):
        self.frame = frame
        self.column_names = column_names

        self.frame.apply_map(lambda x: x.split(","))

    def get_generator(self, batch_size=1000):

        """
            Returns generator which pulls out pandas dataframes of size batch_size from the frame.
        """

        def _generator():

            while 1:

                chunk = self.frame.take(batch_size)

                if len(chunk) == 0:
                    break

                yield chunk

        return _generator()
