# Potato
---

Potato is a framework for streaming and performing operations on multiple
text files on a single machine.


## Example.

###### demo.py

```python
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

```

###### output

```
INFO:potato.backend.search_utils:Found 2742 data files under /home/adityas/nltk_data.
INFO:potato.datastruct.frame:Frame <potato.datastruct.frame.Frame object at 0x7efd5cb9d0f0> initialised with streamer <potato.backend.streamer.Streamer object at 0x7efd5cb9d208>.
INFO:potato.datastruct.frame:Potato context set at directory /home/adityas/nltk_data for files ['\\S*\\.txt+$']
Frame <potato.datastruct.frame.Frame object at 0x7efd5cb9d0f0> contains 2742 files.
['in short, this is no time for delay. it is a time for action--strong, forward-looking action on the pending education bills to help bring the light of learning to every home and hamlet in america--strong, forward-looking action on youth employment opportunities; strong, forward-looking action on the pending foreign aid bill, making clear that we are not forfeiting our responsibilities to this hemisphere or to the world, nor erasing executive flexibility in the conduct of our foreign affairs--and strong, prompt, and forward-looking action on the remaining appropriation bills.\n',
"and the film ends exacly as hamlet , when the creature sets both his and his creator's body on fire . \n",
'hamlet is now available in klingon , albeit perhaps not at your local bookstore , and they are working on translating the bible . \n',
"[note : after claiming otherwise , my appetite was indeed whetted by kenneth branagh's hamlet to search out other attempts to translate shakespeare to film in hopes of finding a better mousetrap . \n",
'it might seem peculiar , then , that zeffirelli ever had an interest in translating hamlet for the screen . \n']

```
