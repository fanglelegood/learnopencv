import cv2
import numpy as np

#图像 放大缩小
dog = cv2.imread('./dog.jpg')

# new = cv2.resize(dog, (400,300))

new = cv2.resize(dog, None, fx=0.3 ,fy=0.3 ,interpolation= cv2.INTER_LINEAR) #放大缩小的算法

print(dog.shape)
 
cv2.imshow('dog', dog)

cv2.imshow('new', new)

cv2.waitKey(0)