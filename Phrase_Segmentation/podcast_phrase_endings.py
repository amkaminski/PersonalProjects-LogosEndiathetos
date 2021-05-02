# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 14:31:20 2021

@author: am_ka
"""

import string
import operator 
import nltk
from nltk import word_tokenize 

source = open("podcast_1.txt", "r")
print("\nSource Mat Loaded")

def TagMaker(word):
    text = word_tokenize(word)
    tagged = nltk.pos_tag(text)
    return tagged[0][1]


listed_sentences = []
clean_tokens = []
rec = {}
    
terminal_punct = [".", "?", "!"]

line = []
for sentence in source:
    
    sentence = sentence.split(" ")
    
    for word in sentence:
        line.append(word)
        for char in word:
            if char in terminal_punct:
                listed_sentences.append(line)
                line = []
                
source.close() # Close the sourcefile 

## Process to clear the word of terminal punctuation (imperfect right now)               
line_index = 0
word_index = 0
             
for line in listed_sentences:
    for word in line:
        for char in word:
            if char in terminal_punct:
                listed_sentences[line_index][word_index] = word.translate(str.maketrans('', '', string.punctuation))
        word_index += 1
        
    line_index += 1
    word_index = 0          
        
print("\nSentences Configured")    


## Extract the end pairings  
x = -1
for line in listed_sentences:  
    if len(line) < 3:
        continue
    
    end_pair = line[x - 1] + "/" + line[x]
    
    if end_pair not in rec:
        rec[end_pair] = 1
    else: 
        rec[end_pair] += 1

print("\nRecord Complete")  
  
## Output the 15 word pairings with the highest counts
end_pairs =  dict(sorted(rec.items(), key=operator.itemgetter(1), reverse=True)[:15])
print("\nMost Frequent End Pairings\n" + "-"*26)
print(end_pairs)



## Construct a dictionary now of word-type pairings coupled with their count
## within the prevously constructed dictionary.
codex = {}
for i in rec.keys():
    split_key = i.split("/")
    
    j = TagMaker(split_key[0])
    k = TagMaker(split_key[1])
    
    tag_pair = j + "/" + k
    
    if tag_pair not in codex:
        codex[tag_pair] = 1
    else:
        codex[tag_pair] += 1
        
## Output the 15 word-type pairings with the highest counts   
end_pair_tags =  dict(sorted(codex.items(), key=operator.itemgetter(1), reverse=True)[:15])
print("\nMost Frequent End Pairing Tags\n" + "-"*30)
print(end_pair_tags)