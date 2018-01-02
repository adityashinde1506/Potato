import logging

logger=logging.getLogger(__name__)

from itertools import islice

class Frame:

    def __init__(self,streamer):
        self.streamer=streamer
        self.generator=self.streamer.get_generator()
        logger.info(f"Frame {self} initialised with streamer {streamer}.")

    def apply_map(self,map_func):
        self.generator=map(map_func,self.generator)
        logger.debug(f"Applied {map_func} to frame.")

    def apply_filter(self,filter_func):
        self.generator=filter(filter_func,self.generator)
        logger.debug(f"Applied {filter_func} to frame.")

    def head(self,num_samples):
        '''
            Return a list of num_samples from the stream.
        '''
        heads=islice(self.generator,num_samples)
        return list(heads)

    def collect(self):
        '''
            Returns a list of all data from the generator.
        '''
        list_data=list(self.generator)
        self.generator=self.streamer.get_generator()
        return list_data

    def take(self,num_samples):
        '''
            Run the generator for num_samples and return the output as a
            list.
        '''
        output=[]
        for line in self.generator:
            output.append(line)
            if len(output)==num_samples:
                return output

        return output
