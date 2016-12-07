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

# , u"ж" u"ш",

wf_patterns  = [u"п",  u"пь", u"б", u"бь", u"ф", u"фь", u"в", u"вь", u"т", u"ть", u"д", u"дь", u"с", u"сь", u"з", u"зь", u"шь?", u"жь?", u"к", u"г"]
wf_ipa_equiv = [u"p ", u"pʲ", u"b", u"bʲ", u"f", u"pʲ", u"v", u"vʲ", u"t", u"tʲ", u"d", u"dʲ", u"s", u"sʲ", u"z", u"zʲ", u"ʂ",   u"ʐ",   u"k", u"ɡ"]
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

wf_match_by_text = pd.DataFrame(columns=wf_ipa_equiv)
for t in texts:
  counts = []
  for p in wf_patterns:
    counts.append(len(t.find_word_final(p)))
  cs = pd.Series(counts, index=wf_ipa_equiv, name=str(os.path.basename(t.file()))[:2])
  wf_match_by_text = wf_match_by_text.append(cs)


#print wf_match_by_text

word_final_counts = []
for p in wf_match:
  word_final_counts.append(len(wf_match[p]))
  

s = pd.Series(word_final_counts, index=wf_ipa_equiv)
#print "Word-Final Occurances:"
#print s.to_string()
plt.figure()
s.plot(kind='bar')
#print s
#plt.bar(X, counts, facecolor='#9999ff', edgecolor='white')
#plt.hist(counts, len(wf_patterns))
plt.show()
plt.savefig("output/bar.png", dpi=800)

print wf_match_by_text.to_string()
plt.figure()
wf_match_by_text.plot.box()
plt.savefig("output/boxplot.png", dpi=800)
#for i in wf_match[u"ф"]:
#  print i
