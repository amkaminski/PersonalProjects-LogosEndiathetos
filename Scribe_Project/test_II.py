# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 18:40:37 2021

@author: am_ka
"""

import nltk

def tokenizeWord(word):
    word_tok = nltk.word_tokenize(word)
    return word_tok

def tagPhrase(phrase):
    phrase_tag = nltk.pos_tag(tokenizeWord(phrase))
    return phrase_tag

