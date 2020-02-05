# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 15:45:19 2019

@author: Alex
"""

import cv2
import numpy as np
#a = np.array(aList[]) then they become booliens
#a > 0 gives us an array of booliens
#sum(a > 0) returns all trues
filename = 'Temple.png'
img = cv2.imread(filename)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)
dst = cv2.cornerHarris(gray, 2, 3, 0.04)

#Dilates the markers
dst = cv2.dilate(dst, None)

img[dst>0.01*dst.max()]=[0, 0, 255]

rowSums = []
a = np.array(dst[0])
#for y in range(len(dst)):
        #a = np.array(dst)
print(sum(a > 0))
    
#rowSums = []
#for y in range(len(dst)):
#    rowSums.append(sum(a > 0))
#    
#colSums = []

#for x in range(len(dst[0])):
#    colSums.append(sum(dst[:,x]))
        
#threshold = 30

#TempleWidth = []
#for y in range(len(dst)):
#    TempleWidths=[]
#    for x in range(len(dst[0])):
#        if dst[y, x] > threshold:
#            TempleWidths.append(dst[y, x])
#    TempleWidth.append(int(len(TempleWidths)))
#    
#TempleHeight=[]
#for x in range(len(dst)):
#    TempleHeights=[]
#    for x in range(len(dst[0])):
#        if dst[y, x] > threshold:
#            TempleHeights.append(dst[y, x])
#    TempleHeight.append(int(len(TempleHeights)))

cv2.imwrite('output.jpg', img)