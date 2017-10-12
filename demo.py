#!/usr/bin/env ipython
"""
Created on Thu Nov 26 11:20:05 2016

@author: afromero
"""
import sys
import numpy as np
import matplotlib.pyplot as plt
import pylab as pyl
import cv2 as cv
import os
import glob
os.environ['GLOG_minloglevel'] = '3'
import config as cfg
import time

category = cfg.category
category = sorted(category, key=category.get)
    
def plot_images_prediction(img_, pred, confidence, file_save=""):
  img = img_.astype(np.uint8, copy=True)[:,:,(2,1,0)]
  predicted = 'Predicted Emotion: '+ category[pred]+ '\nConfidence: '+str(np.max(confidence))[:4]+'%'
  plt.title(predicted)
  plt.imshow(img)
  plt.axis('off')
  if file_save!="": pyl.savefig(file_save, dpi=100)	
  plt.show()
    
def test(net, img_file, file_save=""):
  t = time.time()
  img = cv.imread(img_file)
  img_blob, label_blob = get_blobs(img, 0)

  net.blobs['data'].data[...] = img_blob
  net.forward()
  elapsed = time.time() - t
  #print "elapsed time "+str(elapsed)
  confidence = net.blobs['softmax'].data[0]
  confidence = [float("%.2f"%(n*100)) for n in confidence]
  max_label = np.where(np.array(confidence) == np.max(confidence))[0][0]
  plot_images_prediction(img, max_label, confidence, file_save)


if __name__ == '__main__':
  from preparing_blobs import get_blobs
  import caffe
  caffe.set_device(1)
  caffe.set_mode_gpu()

  modeldef    = './model/VGG_Emotions_16_layers_deploy.prototxt'
  modelweight = './model/VGG_Emotions.caffemodel'

  net = caffe.Net(modeldef, modelweight, caffe.TEST)#VGG model for 16 layers

  for img_file in glob.glob('imgs/*.jpg'):
      test(net, img_file)   

  for img_file in glob.glob('imgs/*.png'):
      test(net, img_file)   

