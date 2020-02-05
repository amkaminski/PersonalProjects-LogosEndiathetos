# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 14:30:22 2019

@author: Alex
"""

import cv2
#import numpy as np

def isBlue(px):
    '''return True if blue'''
    b, g, r = px
    truth = b > r + 50 and b > g + 50
    return truth

filename = 'ParthenonMrkd.png'
img = cv2.imread(filename)


h, w = img.shape[:2]
x = w // 2
for y in range(h):
    if isBlue(img[y, x]):       
        break 

stuff = []
for x in range(w):
    if isBlue(img[y,x]):
        stuff.append(x)
        
left = min(stuff)
right = max(stuff)

TempleWidth = right - left
a = TempleWidth // 2
b = (4*a) // 3
center = ((right - left) // 2) + left
c = (5*a) // 3

'''Markers'''
cv2.drawMarker(img, (center + a, y + b), (0, 255, 0), 2)
cv2.drawMarker(img, (center,y), (0, 255, 0), 2)
cv2.drawMarker(img, (center, y + b), (0, 255, 0), 2)
cv2.drawMarker(img, (left, y + b), (0, 255, 0), 2)

'''Circles'''
cv2.circle(img, (center, y + b), c, (0, 0, 255), 2)
#cv2.circle(img, (center + a, y + b), b, (0, 0, 255), 2)
#cv2.circle(img, (center - a, y + b), b, (0, 0, 255), 2)
#
cv2.circle(img, (center, y +b), a, (0, 0, 255), 2)


'''Circumscribed Pythagorean Triangle'''
cv2.line(img, (center - a, y), (center + a, y + (2*b)), (0, 0, 255), 2)
#cv2.line(img, (center - a, y), (center + a, y), (0, 0, 255), 2)
#cv2.line(img, (center + a, y), (center + a, y + (2*b)), (0, 0, 255), 2)


cv2.imwrite('Blue_Output_Parthenon.jpg', img)