# -*- coding: utf-8 -*-
#!/usr/bin/env python
#
# imageGrid.py
# Split an image into grid
# Usage:
#   python imageGrid.py image.jpg 3x4
#

import sys
import os
from PIL import Image

def cropFromTL(image, div_x, div_y):
    """crop image from top-left
    0   1   2
    3   4   5
    6   7   8

    Arguments:
        image {image} -- PIL image object
        div_x {int} -- div x
        div_y {int} -- div y
    """

    img_w, img_h = image.size
    w = img_w//div_x
    h = img_h//div_y    
    for i in range(div_y):
        for j in range(div_x):
            box = (j*w, i*h, (j+1)*w, (i+1)*h)
            yield image.crop(box)

def crop(image, div_x, div_y):
    """crop image
    8   7   6
    5   4   3
    1   2   0
    
    Arguments:
        image {image} -- PIL image object
        div_x {int} -- div x
        div_y {int} -- div y
    """

    img_w, img_h = image.size
    w = img_w//div_x
    h = img_h//div_y    
    for i in range(div_y-1,-1,-1):
        for j in range(div_x-1,-1,-1):
            box = (j*w, i*h, (j+1)*w, (i+1)*h)
            yield image.crop(box)

def cropSquare(image, div_x):
    """crop a square image
    
    Arguments:
        image {image} -- PIL image object
        div_x {int} -- div x
    """

    img_w, img_h = image.size
    w = img_w//div_x
    div_y = img_h//w
    for i in range(div_y-1,-1,-1):
        for j in range(div_x-1,-1,-1):
            box = (j*w, i*w, (j+1)*w, (i+1)*w)
            # yield box
            yield image.crop(box)

def saveGrid(image_fn, div_x, div_y):
    """save an image with grid
    
    Arguments:
        image_fn {str} -- image filename
        div_x {int} -- div x
        div_y {int} -- div y
    
    Returns:
        array -- filename of all images
    """

    
    images = []
    img = Image.open(image_fn)
    print('size:{}'.format(img.size))
    img_w, img_h = img.size
    crop_w = crop_h = img_w//div_x
    # crop_h = img_h//div_y
    # for k, p in enumerate(crop(img, div_x, div_y)):
    # for k, p in enumerate(cropFromTL(img, div_x, div_y)):
    for k, p in enumerate(cropSquare(img, div_x)):
        # print(k,p)
        img = Image.new('RGB', (crop_w,crop_h), 255)
        img.paste(p)
        img.save('grid-{}.jpg'.format(k))
        images.append('grid-{}.jpg'.format(k))
    return images

if __name__ == "__main__":
    image_fn = sys.argv[1]
    div_x = int(sys.argv[2].split('x')[0])
    div_y = int(sys.argv[2].split('x')[1])
    for i in saveGrid(image_fn, div_x, div_y):
        print("Save {} file".format(i))
        # os.remove(i)


