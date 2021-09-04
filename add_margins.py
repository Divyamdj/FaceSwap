import cv2
import numpy as np
import os

path = r'E:/Kroop AI/horse2zebra/downloads/em_final/'
for pic in os.listdir(path):
  filename = path+pic
  # read image
  img = cv2.imread(filename)
  ht, wd, cc= img.shape

  # create new image of desired size and color (white) for padding
  ww = 256
  hh = 256
  color = (255,255,255)
  result = np.full((hh,ww,cc), color, dtype=np.uint8)

  # compute center offset
  xx = (ww - wd) // 2
  yy = (hh - ht) // 2

  # copy img image into center of result image
  result[yy:yy+ht, xx:xx+wd] = img

  # save result
  cv2.imwrite(filename, result)