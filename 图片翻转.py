import cv2
import numpy as np
from PIL import Image
from pylab import *
import os

img=cv2.imread("/home/fangcaojun/Documents/Python/ImageProcess/q/0.png")
cv2.imshow("original",img)

#水平镜像
h_flip=cv2.flip(img,1)
cv2.imshow("Flipped Horizontally",h_flip)

#垂直镜像
v_flip=cv2.flip(img,0)
cv2.imshow("Flipped Vertically",v_flip)

#水平垂直镜像
hv_flip=cv2.flip(img,-1)
cv2.imshow("Flipped Horizontally & Vertically",hv_flip)

#90°翻转图片
img90=np.rot90(h_flip)
img90=Image.fromarray(uint8(img90))
img90.save("/home/fangcaojun/Documents/Python/ImageProcess/q/90°.jpg")

cv2.waitKey(0)
