# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 13:16:38 2021

@author: am_ka
"""

import nltk
#nltk.download('nps_chat')
#posts = nltk.corpus.nps_chat.xml_posts()[:10000]


#def dialogue_act_features(post):
#    features = {}
#    for word in nltk.word_tokenize(post):
#        features['contains({})'.format(word.lower())] = True
#    return features

#def TypeDetect(line):
#        print(classifier.classify(dialogue_act_features(line)))

def tokenizeWord(word):
    word_tok = nltk.word_tokenize(word)
    return word_tok


#featuresets = [(dialogue_act_features(post.text), post.get('class')) for post in posts]
#
#size = int(len(featuresets) * 0.1)
#
#train_set, test_set = featuresets[size:], featuresets[:size]
#
#classifier = nltk.NaiveBayesClassifier.train(train_set)
#
#print(nltk.classify.accuracy(classifier, test_set))
#
#print(classifier.classify(dialogue_act_features("I saw a box.")))