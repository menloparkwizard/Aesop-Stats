#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs
import re

class Text(object):

  def __init__(self, file):
    self.filename = os.path.abspath(file)

  def parse_file(self):
    with codecs.open(filename=self.filename, mode='r', encoding='utf-8') as fh:
      self.lines = fh.read().strip().splitlines()

  def print_file_to_screen(self):
    for line in self.lines:
      print line

  def find_pattern(self, pattern):
    search = re.compile(pattern, re.UNICODE)
    found = 0
    for line in self.lines:
      result = search.findall(line)
      found += len(result)
    return found


if __name__ == '__main__':
  # Development Testing
  t = Text("texts/0.txt")
  t.parse_file()
  t.print_file_to_screen()
  print t.find_pattern(u'е')