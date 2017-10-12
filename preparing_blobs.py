import numpy as np
import cv2 as cv
import sys
sys.path.insert(0, '..')
import config as cfg

def get_resized_image(image):
  im = image.astype(np.float32, copy=True)
  target_size = cfg.vgg_size
  im_new = cv.resize(im, (target_size, target_size), interpolation=cv.INTER_LINEAR)
  im_new -= cfg.PIXEL_MEANS
  #im_new /= cfg.PIXEL_SCALE
  return im_new

def get_blobs(img, label):
  im_new = get_resized_image(img)

  #reshape these things to match the network
  #the image needs a channel swap
  channel_swap = (2, 0, 1)
  im_new = im_new.transpose(channel_swap)
  im_new = im_new.reshape((1, im_new.shape[0], im_new.shape[1], im_new.shape[2]))

  label_new = np.array(label).reshape((1,1,1,-1))

  return im_new, label_new
