import cv2
import numpy as np

dog = cv2.imread('./dog.jpg')

#图的加法运算就是矩阵的加法
# print(dog.shape)

img = np.ones((1050, 1680, 3), np.uint8) *50

cv2.imshow('dog', dog)

result = cv2.add(dog, img)
result2 = cv2.subtract(dog, img)
cv2.imshow('result', result)
cv2.imshow('result2', result2)
cv2.waitKey(0)

# 乘 multiply
#除法 divide

