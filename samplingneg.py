# -*- coding: utf-8 -*-
"""
Created on Thu May 18 14:58:47 2017

@author: inum
"""

import numpy as np
import scipy.misc
from scipy import ndimage
import Image
import cv2
import glob
import os


rgbimgs = glob.glob("/home/inum/Documents/ProjectCV/datasets/mensa_seq0_1.1/rgb/*.ppm")
txtFiles = glob.glob("/home/inum/Documents/ProjectCV/datasets/mensa_seq0_1.1/track_annotations/*.txt")
negSamples = []


for img in rgbimgs:
    negSamples.append(img)
    base = os.path.basename(img)
    name = os.path.splitext(base)[0]
    for txtfile in txtFiles:
        txt = open(txtfile).read()
        if name in txt:
            negSamples.remove(img)
            break
    
print(len(negSamples))
print(negSamples)

for sample in negSamples:
    img = cv2.imread(sample)
    base = os.path.basename(sample)
    for i in range(3):
        yTopleft = 0 + i*np.random.randint(10)
        rgbHeight = 180
        xTopleft = 0 + i*np.random.randint(10)
        rgbWidth = 360
        img_crop = img[yTopleft:yTopleft+rgbHeight, xTopleft:xTopleft+rgbWidth]
        outputFileName = ("/home/inum/Documents/ProjectCV/datasets/mensa_seq0_1.1/cropped_neg/" + str(i) + base)
        cv2.imwrite(outputFileName, img_crop)
