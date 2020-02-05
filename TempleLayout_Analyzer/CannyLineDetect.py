# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 15:48:40 2019

@author: Alex
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('Temple.png', 0)
edges = cv2.Canny(img, 100, 200)

plt.subplot(121), plt.imshow(img, cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(edges, cmap = 'gray')
plt.title('Uncanny Output'), plt.xticks([]), plt.yticks([])

plt.show()
#cv2.imwrite('Uncanny Output.jpg', img)


#Works fine but needs to be callable