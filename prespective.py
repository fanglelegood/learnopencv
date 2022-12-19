import cv2
import numpy as np

#透视变换，有点像手机拍文件自动生成pdf的功能！
img = cv2.imread('shijuan.jpeg')

src = np.float32([[100,200], [620 ,200], [80 ,800], [610 , 810]])
dst = np.float32([[0,0], [700,0], [0,800], [700,800]])
M = cv2.getPerspectiveTransform(src , dst)
new  = cv2.warpPerspective(img , M  ,(700 ,800))

cv2.imshow('orgin', img)
cv2.imshow('new', new)
cv2.waitKey(0)