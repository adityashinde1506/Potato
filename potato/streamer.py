import logging

logger=logging.getLogger(__name__)

class Streamer:
    '''
        Streams lines from given files into chunks of fixed size.
    '''

    def __init__(self,files_list):
        self.files=files_list
        self.filename_iter=iter(self.files)
        self.curr_file=None
        self.__step_filename()

    def __step_filename(self):
        if self.curr_file:
            self.curr_file.close()
        self.curr_file=open(next(self.filename_iter))
        logger.debug(f"Currently reading {self.curr_file}")

    def get_single_line(self):
        if self.curr_file:
            line=self.curr_file.readline()
            if line=='':


    def get_chunk(self,chunk_size=1000):
        '''
            Get chunk_size lines from files.
        '''
