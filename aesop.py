#! /usr/bin/env python

# Standard Python Imports
import os
import glob

# Local Imports
from text import Text

texts = glob.glob("texts/*.txt")
print texts

for text in texts:
  stimulus = Text(text)
  stimulus.parse_file()
  stimulus.print_file_to_screen()