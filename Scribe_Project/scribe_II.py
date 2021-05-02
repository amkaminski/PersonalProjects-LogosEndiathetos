# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 18:50:27 2021

@author: am_ka
"""

import nltk

# Load NLTK Corpus
#from nltk.book import *
#moby_lines = nltk.corpus.gutenberg.sents('melville-moby_dick.txt')
#print("Corpus Loaded")


def tokenizeWord(word):
    word_tok = nltk.word_tokenize(word)
    return word_tok

def tagPhrase(phrase):
    phrase_tag = nltk.pos_tag(tokenizeWord(phrase))
    return phrase_tag

gram = "NP: {<DT>?<JJ>*<NN>}"

def makeTree(sentence, grammar):
    cp = nltk.RegexpParser(grammar)
    tree = cp.parse(tagPhrase(sentence))
    print(tree)
   # tree.draw()

''' 
    Declarative Sentence: subject + verb ... (subj + VERB)
    
    Interrogative Sentence: (word +) auxiliary + subject + verb 
    
    Imperative Sentence: base verb... (+ VERB +)
    
    Exclamative Sentence: 'What' (+ adjective) + noun + subject + verb
                          'How' (+ adjective/adverb) + subject + verb
                            
'''


