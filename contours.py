import cv2
import numpy as np
#读文件
# img = cv2.imread('contours1.png')
img = cv2.imread('hello.png')
#转换成单通道
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#二值化
ret, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

#轮廓查找
contours ,hierarachy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# print(contours)
# #绘制轮廓
# cv2.drawContours(img, co ntours, -1, (0,255,255), 2)

# #计算面积
# area = cv2.contourArea(contours[0])

# #计算周长
# len  = cv2.arcLength(contours[0], True)

# #多边形逼近
# approx = cv2.approxPolyDP(contours[0], 0.01*len, True)

#最小外接矩形
r = cv2.minAreaRect(contours[1])
box = cv2.boxPoints(r)
box = np.int0(box)
cv2.drawContours(img, [box], 0, (0,0,255), 2)

#最大外接矩形
x,y,w,h = cv2.boundingRect(contours[1])
cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)



cv2.imshow('img', img)
# cv2.imshow('binary', binary)
cv2.waitKey(0)



