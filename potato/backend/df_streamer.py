import logging
import pandas
from potato.backend.streamer import Streamer


class NotSupportedError(Exception):
    pass


class DFStreamer(Streamer):

    """
        Streams full dataframes read from csv files.
    """

    def __init__(self, files_list):
        Streamer.__init__(self, files_list)
        self.logger = logging.getLogger(f"{__name__}.{__class__}")

    def get_chunk(self, chunk_size):
        """
            This class reads whole files. So it should not support this method.
        """
        raise NotSupportedError

    def get_single_line(self):
        """
            This class reads whole files. So it should not support this method.
        """
        raise NotSupportedError

    def get_generator(self):

        def _generator():

            while 1:
                try:
                    data = pandas.read_csv(self.curr_file)
                    yield data
                    self._step_filename()

                except Exception as e:
                    self.logger.error(f"{e}")
                    break

        return _generator()
