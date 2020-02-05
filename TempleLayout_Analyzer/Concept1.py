# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 11:02:51 2019

@author: Alex
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

darkSpace = []
whiteSpace = []
otherDark = []

img = Image.open("TempleTeos.jpg")
px = img.getpixel((x, y))
for y in range(img.height):
    for x in range(img.width):
        if px = (255, 255, 255):
            whiteSpace.append(px)
        elif px = (0, 0, 0):
            darkSpace.append(((px),(x, y)))
            otherDark.append(px)


#WidthPeaks = []
otherDark.sort(reverse=True)
            
#dec = zip(TempleWidth, range(len(TempleWidth)))
#for w, p in list(sorted(dec, reverse=True))[:5]:
#    print(w, p)            