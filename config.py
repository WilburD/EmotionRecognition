# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 16:07:28 2015

@author: afromero
"""
import numpy as np
import sys
import os
PIXEL_MEANS = np.array([[[102.9801, 115.946, 122.7717]]])

category = {'Neutral': 0, 'Happy': 1, 'Sad': 2, 'Anger': 3, 'Fear': 4, \
            'Disgust': 5, 'Surprise': 6, 'Contemp': 7}            
vgg_size = 224 #vgg
