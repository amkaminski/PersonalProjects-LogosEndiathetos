''' 02/08/2020 This script processes the Iliad, or it did when I still had Academic-based 
access to the Perseus Database. It reads it as Cards, joins the cards into the actual 
books and stores the books as massive strings in a list. Each book is looped through again
and if a line contiains any mention of Achilles it is processed and its descriptors extracted.'''


# import statements
import xml.etree.ElementTree as ET
import nltk


import sys
#import os
#from nltk.parse import stanford

# global values
file = 'tlg0012.tlg001.perseus-eng3.xml'
ns = {'tei':'http://www.tei-c.org/ns/1.0'}

#definition of positive and negative words
posWords = ['valiant', 'brilliant', 'swift-footed', 'glorious', 'great-hearted', 'godlike', 'godly', 'fair', 'great']
negWords = ['perish', 'perished', 'fatal', 'distressed', 'bitter', 'hollow', 'dead', 'evil']


# Write a function to look for Achilles 

def paraHasAchilles(para):
    #return True if paragraph mentions Achilles
    result = False
    if 'Achil' in para:
        result = True
    #Achilles sometimes referenced as 'Son of Peleus'
    elif 'Peleus' in para:
        result = True

    return result

# main code starts here
# parse XML document
xml = ET.parse(file).getroot()

cards = xml.findall('.//tei:div[@subtype="card"]', ns)
print(len(cards), 'cards found')


# this will hold book data
books = []

#  read book by book    
for book in xml.findall('.//tei:div[@subtype="book"]', ns):
    
    # save the book number
    book_num = book.get('n')

    # this will hold extracted text for this book only
    text_segments = []

    # loop over XML chapter elements in this book
    for card in book.findall('.//tei:div[@subtype="card"]', ns):
        
    # delete notes
        for note in card.findall('note'):
            card.remove(note)

    # extract text
    this_text = ' '.join(card.itertext())

    # add to long string
    text_segments.append(this_text)


    book_text = ' '.join(text_segments)
    
    
    
    books.append(book_text)

     # do nlp stuff
     # this will hold nounds and adjs for this book

    adjs = []
    nouns = []

    # segment each book into sentences
    sentences = nltk.sent_tokenize(book_text)
    
    charCount = 0
    # loop over sentences
    for sentence in sentences:
        for word in sentences:
            for char in word:
                charCount = charCount + 1
                
        # only consider sentences mentioning achilles
        if paraHasAchilles(sentence):

            # tokenize & pos-tag
            tokens = nltk.word_tokenize(sentence)
            tagged = nltk.pos_tag(tokens)

            # check for adjs and nouns, then store them
            for tok, pos in tagged:

                if pos == 'JJ':
                    adjs.append(tok)

                elif pos.startswith('NN'):
                    nouns.append(tok)

# count pos, neg words
# initialize counts

    posCount = 0
    negCount = 0

# count positive descriptors
    for w in posWords:
        posCount = posCount + adjs.count(w)

    # count negative descriptors
    for w in negWords:
        negCount = negCount + adjs.count(w)

    print('{}\t{}\t{}'.format(book_num, posCount, negCount))

    