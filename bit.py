import cv2
import numpy as np

#非操作

img = np.zeros((200, 200), np.uint8)
img2 = np.zeros((200,200), np.uint8)

img[20:120 , 20:120] = 200
img2[80:180 , 80:180] = 255

# new_img = cv2.bitwise_not(img)  #取非反转颜色
# new_img = cv2.bitwise_and(img, img2)
# new_img = cv2.bitwise_or(img, img2)
new_img = cv2.bitwise_xor(img, img2)  #异或 白色相同的部位变成黑色，但是黑色相同的地方还是黑色啥情况？

cv2.imshow('new_img' , new_img)
cv2.imshow('img' , img)
cv2.imshow('img2' , img2)
cv2.waitKey(0)