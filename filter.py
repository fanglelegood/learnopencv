import cv2
import numpy as np
img = cv2.imread('car.jpeg')

#filter2d 均值滤波

# kernal = np.ones((5,5), np.float32) /25

# dst = cv2.filter2D(img, -1 , kernal)

# boxFilter  方盒滤波
# dst = cv2.blur(img, (5,5))  #均值滤波

# dst = cv2.GaussianBlur(img, (5,5) ,sigmaX= 0.1)  #高斯滤波，，去除噪点

# dst = cv2.medianBlur(img , 5)  #中值滤波，，去除胡椒噪点

# dst = cv2.bilateralFilter(img, 7 , 20 ,50)  #双边滤波，，特别对美颜有效果！。

#漏掉一级 索贝尔算子  以下都是边缘检测  以下三个都是高斯滤波
# dst = cv2.Sobel( src, ddepth, dx, dy[,ksize[, scale[, delta[, borderType]]]] )
#sobelx = cv2.Sobel(img,cv2.CV_64F,1,0)
# d1 = cv2.Sobel(img , cv2.CV_64F, 1 ,0 , ksize = 5)
# d2 = cv2.Sobel(img , cv2.CV_64F, 0 ,1 , ksize = 5)
# dst = cv2.add(d1, d2)

# Scharr 算子
# d1 = cv2.Scharr(img , cv2.CV_64F, 0, 1)
# d2 = cv2.Scharr(img , cv2.CV_64F, 1, 0)
# dst = cv2.add(d1, d2)

# 拉普拉斯算子 （之前先去噪 受噪音影响大） 更简单，无需X Y分别计算
# dst = cv2.Laplacian(img , cv2.CV_64F, ksize = 5)

# canny边缘检测
dst = cv2.Canny(img, 50, 70)


cv2.imshow('img', img)
cv2.imshow('dst', dst)
cv2.waitKey(0)