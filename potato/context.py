import logging
from potato.backend import get_data_files
from potato.backend import Streamer
from potato.datastruct import Frame

logger = logging.getLogger(__name__)


class Context:
    '''
        This is a context object. It creates frame and streamer objects on
        the backend.
    '''

    def __init__(self, directory, files):
        '''
            Create streamer and frame objects.
        '''

        assert type(directory) == str, "Directory param should be a string."
        assert type(files) == list, "Files param should be a list."

        self.files = get_data_files(directory, files)
        self.streamer = Streamer(self.files)
        self.frame = Frame(self.streamer)
        logger.info(f"Potato context set at directory {directory} for files {files}")

    def get_streamer(self):
        '''
            Return self.streamer for diret access.
        '''

        return self.streamer

    def get_frame(self):
        return self.frame

    def get_dframe(self, column_names, seperator=",", skip_title=True):
        return DFrame(self.streamer, column_names=column_names, seperator=seperator, skip_title=skip_title)
