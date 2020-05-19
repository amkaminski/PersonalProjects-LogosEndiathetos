# -*- coding: utf-8 -*-
"""
Created on Sat May 16 12:51:16 2020

@author: am_ka
"""

import nltk
from nltk.book import *

moby_lines = nltk.corpus.gutenberg.sents('melville-moby_dick.txt')
print("Corpus Loaded")

# Stores each encoded sentence
codex = []
# Stores each unique sentence code
reference = []

#
# Iterate through each sentence initiate an empty string and iterate through
# each word. Tokenize/tag each word and add the tags denoting an adjective,
# noun, verb or adverb to the empty string, creating a sequence of tags that 
# denotes the basic structure of that sentence. Add the sequence to the codex 
# list.
# 

count = 0
for lines in moby_lines:
   sequence = ''
   for i in lines:
       count += 1
       print("Processing Word " + str(count) + ': ' + i)
       token = nltk.word_tokenize(i)
       tagged = nltk.pos_tag(token)
       for tok, tag in tagged:
           if tag.startswith('JJ'):
               sequence += '(JJ)'
           elif tag.startswith('NN'):
               sequence += '(NN)'
           elif tag.startswith('V'):
               sequence += '(V)'
           elif tag.startswith('R'):
               sequence += '(R)'
   codex.append(sequence)     
           
print("Codex Complete")      

# Compile an alternate list of unique existing sequences.   
for i in codex:
    if i in reference:
        pass
    else:
        reference.append(i)
        
print("Reference Complete")

# Compare the amount of sentence sequences with individual known sequences.
print("Length of Codex: " + str(len(codex)))
print("Length of Reference: " + str(len(reference)))



