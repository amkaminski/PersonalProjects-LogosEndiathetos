import cv2
import numpy as np
from matplotlib import pyplot as plt

#
# Load the image
#

img = cv2.imread('TempleTeos.jpg')
grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

kernel = np.ones((5, 5))
eroded = cv2.dilate(grey, kernel)

# Otsu's thresholding after Gaussian filtering
#   - see https://docs.opencv.org/3.4.0/d7/d4d/tutorial_py_thresholding.html
ret, b_w = cv2.threshold(eroded, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

dilated = cv2.erode(b_w, kernel)

plt.figure(figsize=(15,10))
plt.subplot(1, 2, 1)
plt.imshow(eroded)
plt.subplot(1, 2, 2)
plt.imshow(dilated)


#
# Find the cella wall in the y dimension
#

# image dimensions
height, width = b_w.shape
center = width // 2

# this offset is one-half the height of the rectangular sample that constitutes a "core"
v_offset = 5 # arbitrary
# this is one-half the width of the core
h_offset = width // 20 # 5 percent of the image width


# traverse the y dimension of the image, travelling down the centre
#   - take "cores" at each y position
cores = []

for y in range(v_offset, height-v_offset):
    
    # calculate sides of the core sample rectangle
    left = center - h_offset
    right = center + h_offset
    top = y - v_offset
    bottom = y + v_offset
    
    # add the pixels values within the sample
    core = sum(np.ravel(b_w[top:bottom, left:right]))
    
    # collect the core
    cores.append(core)
    
# FIXME: x pos of the cella wall is center of the image
wall_x = center
# y pos of the cella wall is the minimum core value (most black pixels), plus offset
wall_y = np.argmin(cores) + v_offset

# annotate the image
img_annotated = img.copy()
cv2.circle(img_annotated, (wall_x, wall_y), 10, (255, 0, 0), 5)
plt.imshow(img_annotated)


#
# Calculate the length of the cella wall, find true center
#

# get continuous black segments along a given x

# start (i.e. left edge) of each segment
starts = []
# length of each segment
lens = []

# when this is True, we're in the middle of a seg
going = False

# traverse the cross-section:
#   - if the pixel is white
#        any ongoing segment is finished
#   - if the pixel is black
#        any ongoing segment is continued
#        otherwise, a new segment is started
for x in range(width):
    if b_w[wall_y, x] > 0:
        going = False
    else:
        if going:
            lens[-1] += 1
        else:
            lens.append(1)
            starts.append(x)
            going = True

# which seg is the longest one?
i = np.argmax(lens)

# figure out edges of the cella
left = starts[i]
center = left + lens[i] // 2

# new annotated image
img_annotated = img.copy()
cv2.circle(img_annotated, (center, wall_y), 10, (255, 0, 0), 5)
plt.imshow(img_annotated)