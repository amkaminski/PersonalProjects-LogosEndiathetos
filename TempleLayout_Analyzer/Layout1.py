# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 22:40:03 2019

@author: Alex
"""
from PIL import Image

layout = Image.open('Temple.PNG')

def Layout(pic):
    
    newImage = Image.new('RGB', (pic.size))

    for x in range(newImage.width):
        for y in range(newImage.height):
            newImage.putpixel((x, y), (pic.getpixel((x, y))))

    return newImage