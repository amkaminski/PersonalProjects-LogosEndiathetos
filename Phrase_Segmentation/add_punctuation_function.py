# -*- coding: utf-8 -*-
"""
Created on Thu June 18 09:24:33 2020

@author: am_ka
"""

''' Testing Function to add periods to text-from-speech'''

import nltk 

def PhraseMaker(text):
    phrase = text.split(' ') # Convert a string to a list
    precursor = [('X', 'Y')] # The initial 'precursor' value is arbitrary, it will
                             # denote the word type that comes before 'i'
                             
    word = 0 # keeps track of sentence length
    for i in phrase:
        
        word_tagged = nltk.pos_tag(nltk.word_tokenize(i))
        
        if not word_tagged: # Test for empty list
            continue
        
        else:
            word += 1
            print("{0}: {1} {2}".format(word, word_tagged[0][0], word_tagged[0][1]))
            # Feasible word-type pairings based off the findings in 'mobydick_phrase_endings.py'
            pair1 = precursor[0][1].startswith('DT') and word_tagged[0][1].startswith('NN')
            pair2 = precursor[0][1].startswith('NN') and word_tagged[0][1].startswith('NN')
            pair3 = precursor[0][1].startswith('IN') and word_tagged[0][1].startswith('NN')
            # 'pair4' mostly for testing purposes, matching at least one position in the test phrase 'words'
            pair4 = precursor[0][1].startswith('DT') and word_tagged[0][1].startswith('IN')
            pair5 = precursor[0][1].startswith('PRP$') and word_tagged[0][1].startswith('NN')
            pair6 = precursor[0][1].startswith('IN') and word_tagged[0][1].startswith('DT')
            
            # Ascertain whether or not 'precursor' and 'word_tagged' represent the types of 
            # words that would typically conclude a sentence
            right_pair = pair1 or pair2 or pair3 or pair4 or pair5 or pair6
            
            # If the pair matches any of the specified patterns and are within range of 
            # the average lengths of sentences, add a period and reset the count
            if word in range(10, 16) and right_pair:
                phrase[phrase.index(i)] += '.'
                word = 0
        
        precursor = word_tagged
        
    # Produce the phrase with the inserted punctuation   
    return " ".join(phrase)
    
    
words = ("I am really sorry you had to spend time figuring this out "
        "I understand this must be frustrating for you I really appreciate "
        "your help and I know it’s stressful when you’ve got work to do and "
        "you’re stuck like this As soon as you reply I’ll be automatically "
        "notified so I can start investigating for you")

print("\n" + PhraseMaker(words) + "\n")


transcript_1 = ("Yeah, I think I largely do The uncomfortable thing for me "
                "I think is when I'm afraid I'm gonna make the other person "
                "feel uncomfortable Cause you know I bring up my dead mom, it's "
                "like the air gets sucked out of the room So I, I mostly want to "
                "be able to just talk about it and feel comfortable sharing this "
                "truth about my life and not make everyone sad or scared "
                "or uncomfortable")

print("\n" + PhraseMaker(transcript_1) + "\n")