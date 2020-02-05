# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 14:44:22 2018

@author: Alex
"""
#import requests
url = 'http://www.perseus.tufts.edu/hopper/xmlchunk?doc=Perseus%3Atext%3A1999.01.0134%3Abook%3D1%3Acard%3D1'

response = requests.get(url)

if not response.ok:
    response.raise_for_status()
    
file = open('iliad-perseus.xml', 'wb')
file.write(response.content)
file.close()

from xml.etree import ElementTree as ET

doc = ET.parse('iliad-perseus.xml').getroot()

chaps = doc.findall('.//div1[@type="chapter"]')
print("Found", len(chaps), "chapters.")

plaintext = []

for chap in chaps:
    for note in chap.findall('note'):
        chap.remove(note)
        
    this_text= '  '. join(chap.itertext())
    plaintext.append(this_text)
    
iliad = '  '.join(plaintext)

print(len(iliad))