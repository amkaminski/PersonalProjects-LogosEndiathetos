# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 14:07:06 2019

@author: Alex
"""

import cv2
import numpy as np
#a = np.array(aList[]) then they become booliens
#a > 0 gives us an array of booliens
#sum(a > 0) returns all trues
filename = 'TempleTeos.jpg'
img = cv2.imread(filename)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)
dst = cv2.cornerHarris(gray, 2, 3, 0.04)

#Dilates the markers
dst = cv2.dilate(dst, None)

img[dst>0.01*dst.max()]=[0, 0, 255]

threshold = 30

TempleWidth = []
for y in range(len(dst)):
    TempleWidths=[]
    for x in range(len(dst[0])):
        if dst[y, x] > threshold:
            TempleWidths.append(dst[y, x])
    TempleWidth.append(int(len(TempleWidths)))
    
TempleHeight=[]
for x in range(len(dst[0])):
    TempleHeights=[]
    for y in range(len(dst)):
        if dst[y, x] > threshold:
            TempleHeights.append(dst[y, x])
    TempleHeight.append(int(len(TempleHeights)))

WidthPeaks = []
TempleWidth.sort(reverse=True)
#WidthPeaks.append(TempleWidth[0])
#WidthPeaks.append(TempleWidth[1])
#WidthPeaks.append(TempleWidth[:10])

#dec = zip(TempleWidth, range(len(TempleWidth)))
#for w, p in list(sorted(dec, reverse=True))[:5]:
#    print(w, p)

#len(img_dilation)

#Take the two spikes from each list
#and use the (x, y) vals of each to 
#determine edges of the temple stylobate
cv2.imwrite('output_TempleTeos.jpg', img)