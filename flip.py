import cv2
import numpy as np

#图像翻转
dog = cv2.imread('./dog.jpg')
new = cv2.flip(dog , 0)
new1 = cv2.flip(dog, 1)

cv2.imshow('dog', dog)
cv2.imshow('new1', new1)
cv2.waitKey(0)