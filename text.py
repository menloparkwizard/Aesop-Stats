#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs
import re

class Text(object):

  def __init__(self, file):
    self.filename = os.path.abspath(file)
    self.words    = []

  def parse_file(self):
    with codecs.open(filename=self.filename, mode='r', encoding='utf-8') as f:
      self.lines = f.read().strip().splitlines()
    
    for line in self.lines:
      if line.strip(): # remove blank lines
        self.words.extend(line.split(' '))

  def word_count(self):
    return len(self.words)

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

  def find_word_final(self, pattern):
    valid = re.compile(u"\w+{0}".format(pattern), re.UNICODE)
    valid_words = []
    for line in self.lines:
      result = valid.findall(line)
      if(result is not None):
        valid_words.extend(result)
    return valid_words

  def count_glyphs(self):
    num_glyphs = 0
    for word in self.words:
      num_glyphs += len(word)
    return num_glyphs

  def unique_glyphs(self):
    unique = []
    for word in self.words:
      glyphs = list(self.__remove_punctuation(word).lower())
      for glyph in glyphs:
        if glyph not in unique:
          unique.append(glyph)
    return unique

  def glyph_frequency(self):
    glyph_freq = {}
    for word in self.words:
      glyphs = list(self.__remove_punctuation(word).lower())
      for glyph in glyphs:
        if glyph not in glyph_freq:
          glyph_freq[glyph] = 1
        else:
          glyph_freq[glyph] += 1
    return glyph_freq

  def count_words(self):
    num_words = len(self.words)
    return num_words

  def unique_words(self):
    unique = []
    for word in self.words:
      word = self.__remove_punctuation(word).lower()
      if word not in unique:
        unique.append(word)
    return unique

  def word_frequency(self):
    word_freq = {}
    for word in self.words:
      word = self.__remove_punctuation(word).lower()
      if word not in word_freq:
        word_freq[word] = 1
      else:
        word_freq[word] += 1
    return word_freq


  # Private Helper Functions
  def __remove_punctuation(self, word):
    return re.sub(u'[.,!\'?]', "", word) # remove punctuation


if __name__ == '__main__':
  # Development Testing
  t = Text("texts/00.txt")
  t.parse_file()
  #t.print_file_to_screen()
  #print "Found: " + str(t.find_pattern(u'е')) + " of " + u'е'
  #print "Counted: " + str(t.count_glyphs()) + " glyphs"
  #print "Words: " + str(t.count_words())
  #print "Unique words: " + str(len(t.unique_words()))
  #print "Unique glyphs: " + str(len(t.unique_glyphs()))
  #print t.glyph_frequency()
  #print t.word_frequency()
  wf_match = t.find_word_final(u"ом")
  for m in wf_match:
    print m
  #print wf_match
  print "Found: " + str(len(wf_match)) + " words out of " + str(t.word_count())

