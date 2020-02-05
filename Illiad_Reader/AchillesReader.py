# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 15:56:57 2018

@author: Alex
"""

import xml.etree.ElementTree as ET
import nltk
import os
from nltk.parse import stanford

file = 'tlg0012.tlg001.perseus-eng3.xml'
ns = {'tei':'http://www.tei-c.org/ns/1.0',}
xml = ET.parse(file).getroot()
cards = xml.findall('.//tei:div[@subtype="card"]', ns)
print(len(cards), 'cards found')
    
para = []
for card in cards:
    para.append(' '.join(card.itertext()))
    
plaintext = []
# loop over xml chapter elements
for card in cards:
    # delete notes
    for note in card.findall('note'):
        card.remove(note)
    # extract text
    this_text = ' '.join(card.itertext())
    # add to long string
    plaintext.append(this_text)
    
# now paste it all together
iliad = ' '.join(plaintext)    

#look for Achilles
def paraHasAchilles(para):
    
    result = False
    
    if 'Achil' in para:
        result = True
    elif 'Peleus' in para:
        result = True
    
    return result

sentences = nltk.sent_tokenize(iliad)
tokens = nltk.word_tokenize(sentences[2])
tagged = nltk.pos_tag(tokens)

adjs = []
nouns = []

for sentence in sentences:
    if paraHasAchilles(sentence):
        tokens = nltk.word_tokenize(sentence)
        tagged = nltk.pos_tag(tokens)
        for tok, pos in tagged:
            if pos == 'JJ':
                adjs.append(sentence)
            elif pos.startswith('NN'):
                nouns.append(sentence)
#print('adjs: ', adjs) 
#print('nouns: ', nouns)
                
def sections(l, n):
    #Yield successive n-sized chunks from l.
    for i in range(0, len(l), n):
        yield l[i:i + n]
        
posWords = "valiant brilliant swift-footed glorious great-hearted godlike godly fair great"
negWords = "perish perished fatal distressed bitter hollow dead evil"

numb = 0

for i in sections(adjs, 100):
    numb = numb + 1
    posCount = 0
    for adj in posWords.split():
        posCount = posCount + adjs.count(adj)
    negCount = 0
    for adj in negWords.split():
        negCount = negCount + adjs.count(adj)
    print('posCount', numb, ':', posCount)
    print('negCount', numb, ':', negCount)
    
    













