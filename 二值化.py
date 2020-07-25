import cv2 as cv
import numpy as np
import os

#全局阈值
def threshold_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_RGB2GRAY)  #把输入图像灰度化
    #直接阈值化是对输入的单通道矩阵逐像素进行阈值分割。
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_TRIANGLE)
    print("threshold value %s"%ret)

    #cv.namedWindow("binary0", cv.WINDOW_NORMAL)
    #cv.imshow("binary0", binary)

    return binary

#局部阈值
def local_threshold(image):
    gray = cv.cvtColor(image, cv.COLOR_RGB2GRAY)  #把输入图像灰度化
    #自适应阈值化能够根据图像不同区域亮度分布，改变阈值
    binary =  cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY, 25, 10)
    #cv.namedWindow("binary1", cv.WINDOW_NORMAL)
    #cv.imshow("binary1", binary)
    return binary

#用户自己计算阈值
def custom_threshold(image):
    gray = cv.cvtColor(image, cv.COLOR_RGB2GRAY)  #把输入图像灰度化
    h, w =gray.shape[:2]
    m = np.reshape(gray, [1,w*h])
    mean = m.sum()/(w*h)
    print("mean:",mean)
    ret, binary =  cv.threshold(gray, mean, 255, cv.THRESH_BINARY)
    #cv.namedWindow("binary2", cv.WINDOW_NORMAL)
    #cv.imshow("binary2", binary)
    return binary


dir_path='/home/fangcaojun/Documents/Python/ImageProcess/InputImages/'
out_path='/home/fangcaojun/Documents/Python/ImageProcess/OutputImages/'
cnt=len(os.listdir(dir_path))-1

for i in range(1,cnt):
    input_im = cv.imread(dir_path+'%03d.jpg'%i)
    output_im=custom_threshold(input_im)

    cv.imwrite(out_path+'%04d.jpg'%i,output_im)
    
