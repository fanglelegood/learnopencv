import cv2
import numpy as np

img = np.zeros((480, 640 ,3) ,np.uint8)

#画线
cv2.line(img, (10, 20), (300,400), (0,0,255), 5, 4)

#画圆
cv2.circle(img, (320, 240), 100, (0,0,255))
cv2.circle(img, (320, 240), 25, (0,0,255), -1)

#画椭圆
cv2.ellipse(img, (320, 240), (100, 50) , 0 ,0 , 360, (0, 0,255))

#画多边形
pts = np.array([(300, 10), (150,100) ,(450,100)], np.int32)  #不可以是uint
cv2.polylines(img, [pts], True, (0,0,255))
cv2.fillPoly(img, [pts], (0,255,255))

#绘制文本
cv2.putText(img,"HEllomiao" , (10,400), 4, 3, (255,255,255))


cv2.imshow('draw' , img)
cv2.waitKey(0)