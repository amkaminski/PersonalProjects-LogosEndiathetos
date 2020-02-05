# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 15:48:40 2019

@author: Alex
"""

import cv2
import numpy as np

filename = 'Temple.png'
img = cv2.imread(filename)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)
dst = cv2.cornerHarris(gray, 2, 3, 0.04)

#Dilates the markers
dst = cv2.dilate(dst, None)

img[dst>0.01*dst.max()]=[0, 0, 255]

#img[dst(1)>0.01*dst.max()]=[255, 0, 0]


#cv2.imshow('dst', img)
#if cv2.waitKey(0) & 0xff == 27:
#    cv2.destroyAllWindows()
flag = False 
#colSums = []
#rowSums = []
rowLength = 0
colLength = 0
#for y in range(len(dst)):
    #rowSums.append(sum(dst[y]))
    #for x in range(len(dst[y])):
        #if dst[y, x] > 0:
            
#            #img[y, x]= [255, 0, 0]
#            cv2.circle(img, (x,y), 40, (255, 0, 0), 5)
#            print(x, y)
#            flag = True
#            break
#    if flag: 
#        break
TempleWidth = []
for y in range(len(dst)):
    TempleWidths=[]
    for x in range(len(dst)):
        if dst[y, x] > 0:
            TempleWidths.append(dst[y, x])
    TempleWidth.append(int(len(TempleWidths())))
           
print(rowLength)
cv2.imwrite('output.jpg', img)            