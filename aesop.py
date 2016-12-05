#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Standard Python Imports
import os
import sys
import codecs
import glob
import matplotlib.pyplot as plt

# Local Imports
from text import Text

# set default output encoding so we can pipe to files
sys.stdout = codecs.getwriter('utf8')(sys.stdout)

text_files = glob.glob("texts/*.txt")
print text_files

wf_patterns = [u"п", u"пь", u"б", u"бь", u"ф", u"фь", u"в", u"вь", u"т", u"ть", u"д", u"дь", u"с", u"сь", u"з", u"зь", u"ш", u"шь", u"ж", u"жь", u"к", u"г"]

print "Checking: " + str(len(wf_patterns)) + " patterns"

# Parse all the text files
texts = []
for f in text_files:
  T = Text(f)
  T.parse_file()
  texts.append(T)
  #stimulus.parse_file()
  #stimulus.print_file_to_screen()

wf_match = {}

for p in wf_patterns:
  print "Searching for: " + p
  for t in texts:
    if p in wf_match:
      wf_match[p].extend(t.find_word_final(p))
    else:
      wf_match[p] = t.find_word_final(p)
    print "Found: " + str(len(t.find_word_final(p))) + " matches in " + t.file()


for p in wf_match:
  print "Found: " + str(len(wf_match[p])) + " matches for " + p
  #for t in wf_match[p]:
   #print t

for i in wf_match[u"ф"]:
  print i