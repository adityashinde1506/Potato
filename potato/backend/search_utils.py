import logging

logger=logging.getLogger(__name__)

from pathlib import Path
from itertools import cycle
import re

def path_visitor(path,names,found):
    '''
        Recursively traverses directory and looks for given files.
    '''
    for name in names:
        if re.match(name,path.parts[-1]):
            logger.debug(f"Found file {str(path)}")
            found.append(str(path))
    if not path.is_dir():
        return
    for _path in path.iterdir():
        path_visitor(_path,names,found)

def get_data_files(entry_dir,filenames):
    '''
        Recursively traverses entry_dir to find all filenames.
        Returns full path of found filenames.
    '''
    assert type(entry_dir)==str, "Entry directory should be a string."
    entry_dir=Path(entry_dir)

    found=[]
    path_visitor(entry_dir,filenames,found)
    logger.info(f"Found {len(found)} data files under {str(entry_dir)}.")
    return found
