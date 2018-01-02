import logging
import sys

logging.basicConfig(level=logging.INFO)
sys.path.append("/home/adityas/Projects/Potato")

from potato import Context

path="/home/adityas/nltk_data"
files=r"\S*\.txt+$"

context=Context(path,[files])
frame=context.get_frame()

print(f"Frame {frame} contains {frame.get_num_files()} files.")

frame.apply_map(lambda x:x.lower())
frame.apply_filter(lambda x:"hamlet" in x)

print(frame.head(5))
