#! /usr/bin/env python

import os
import codecs
import pprint

class Text(object):

  def __init__(self, file):
    self.filename = os.path.abspath(file)

  def parse_file(self):
    with codecs.open(filename=self.filename, mode='r', encoding='utf-8') as fh:
      self.lines = fh.read().strip().splitlines()

  def print_file_to_screen(self):
    for line in self.lines:
      print line


if __name__ == '__main__':
  # Development Testing
  t = Text("texts/0.txt")
  t.parse_file()
  t.print_file_to_screen()
