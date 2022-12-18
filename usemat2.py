import cv2
import numpy as np

img = cv2.imread('D:\\opencv\jpg\R-C.jpg')

print(img.shape)

#图像占用空间
print(img.size)

#元素位深
print(img.dtype)