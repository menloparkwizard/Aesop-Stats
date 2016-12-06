#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Standard Python Imports
import os
import sys
import codecs
import glob
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

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

wf_match = {}
# wf_match_by_text = {}
for p in wf_patterns:
  print "Searching for: " + p
  for t in texts:
    if p in wf_match:
      wf_match[p].extend(t.find_word_final(p))
    else:
      wf_match[p] = t.find_word_final(p)
    print "Found: " + str(len(t.find_word_final(p))) + " matches in " + t.file()
    # file = str(os.path.basename(t.file()))[:2]
    # if file in wf_match_by_text:
    #   wf_match_by_text[file].append({ p : len(t.find_word_final(p))})
    # else:
    #   wf_match_by_text[file] = [{ p : len(t.find_word_final(p))}]

wf_match_by_text = pd.DataFrame(columns=wf_patterns)
for t in texts:
  counts = []
  for p in wf_patterns:
    counts.append(len(t.find_word_final(p)))
  cs = pd.Series(counts, index=wf_patterns, name=str(os.path.basename(t.file()))[:2])
  wf_match_by_text = wf_match_by_text.append(cs)


#print wf_match_by_text

word_final_counts = {}
for p in wf_match:
  word_final_counts[p] = len(wf_match[p])
  

s = pd.Series(word_final_counts)
#print "Word-Final Occurances:"
#print s.to_string()
plt.figure()
s.plot(kind='bar')
#print s
#plt.bar(X, counts, facecolor='#9999ff', edgecolor='white')
#plt.hist(counts, len(wf_patterns))
#plt.show()
plt.savefig("output/bar.png", dpi=800)

print wf_match_by_text.to_string()
plt.figure()
wf_match_by_text.plot.box()
plt.savefig("output/boxplot.png", dpi=800)
#for i in wf_match[u"ф"]:
#  print i
