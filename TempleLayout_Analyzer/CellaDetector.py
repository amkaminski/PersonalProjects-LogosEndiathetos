# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 13:50:31 2019

@author: Alex
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

filename = 'AnotherTemple.png'
img = cv2.imread(filename)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)
dst = cv2.cornerHarris(gray, 2, 3, 0.04)

kernel = np.ones((5, 5), np.uint8)

#Dilates the markers
dst = cv2.dilate(dst, None)

img[dst>0.01*dst.max()]=[0, 0, 255]

v_offset = 5

cores = []
img_dilation = cv2.dilate(img, kernel, iterations = 2)

for y in range(v_offset, len(img_dilation)-v_offset):
    w = len(img_dilation[y])
    c = w // 2
    l = c - w // 20
    r = c + w // 20
    t = y - v_offset
    b = y + v_offset
    
    core = sum(np.ravel(img_dilation[t:b, l:r]))
    
    cores.append(core)
    
plt.plot(cores)


wall_x = img_dilation.shape[1] // 2
wall_y = np.argmin(cores) + v_offset

img_annotated = img_dilation.copy()
cv2.circle(img_annotated, (wall_x, wall_y), 10, (255, 0, 0), 5)
plt.imshow(img_annotated)
cv2.imwrite('output_AnotherOutput.jpg', img_annotated)

starts = []
lens = []
going = False

for x in range(len(img_dilation[wall_y])):
    if img_dilation[wall_y, x] > 0:
        going = False
    else:
        if going:
            lens[-1] += 1
        else:
            lens.append(1)
            starts.append(x)
            going = True
           
