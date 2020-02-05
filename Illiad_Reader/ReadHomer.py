# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 11:26:36 2018

@author: Alex
"""

#import statements


import xml.etree.ElementTree as ET
import nltk

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
#import os
#from nltk.parse import stanford
    
sentences = nltk.sent_tokenize(iliad)

tokens = nltk.word_tokenize(sentences[2])

#this is where we have a problem
tagged = nltk.pos_tag(tokens)

adjs = []
nouns = []

#for para in iliad:
    #if paraHasAchilles(para):
        
        #for tok, pos in tagged: 
            #if pos == 'JJ':
                #adjs.append(tok)
            #elif pos.startswith('NN'):
                #nouns.append(tok)
                
    #print('adjs: ', adjs)
    #print('nouns: ', nouns)
                        

for sentence in sentences:
    if paraHasAchilles(sentence):
        tokens = nltk.word_tokenize(sentence)
        tagged = nltk.pos_tag(tokens)
        for tok, pos in tagged:
            if pos == 'JJ':
                adjs.append(tok)
            elif pos.startswith('NN'):
                nouns.append(tok)

#print('adjs: ', adjs) 
#print('nouns: ', nouns)               
 
def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]
             
#counter = 0
step = 100
posWrds = []
negWrds = []

counter = 0
for word in adjs:
    counter = counter + 1
    #correct operator for divisible by 100?    
    if counter % step == 0:
        #if a word matches a word in "posWords" increase a count and add that count to a list
        
           
            
        
posWords = "valiant, brilliant, swift-footed, glorious, great-hearted, godlike, godly, fair, great"
negWords = "perish, perished, fatal, distressed, bitter, hollow, dead, evil"




#posCount = 0
#negCount = 0

#adj = str(adjs)
#non = str(nouns)



#for word in adj:
    #for i in posWords.split():
        #posCount = 0
        #test = []
        #if word == i:
            #posCount = posCount + 1
            #test.append(word)
#print('PosCount: ', posCount)
            
#for word in non:
    #for i in negWords.split():
        #negCount = 0
        #if word == i:
            #negCount = negCount + 1
#print('NegCount: ', negCount)
        

    









    