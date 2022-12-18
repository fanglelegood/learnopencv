import cv2
import numpy as np
#旋转图像 ，变换矩阵API
dog = cv2.imread('./dog.jpg')
h ,w ,ch = dog.shape
# M = np.float32([[1, 0 ,500], [0,1,300]])
#旋转的角度是逆时针
# M = cv2.getRotationMatrix2D((w/2, h/2), 15 ,0.3)

#第二种变换矩阵的方法，，有横竖两条线。。
src = np.float32([[400,300], [800, 300], [400, 1000]])
dst = np.float32([[200,400], [600, 500], [150, 1100]])

M = cv2.getAffineTransform(src, dst)
#改变新图像尺寸改 下面的 w和h
new = cv2.warpAffine(dog, M, (w, h))

cv2.imshow('dog', dog)
cv2.imshow('new', new)

cv2.waitKey(0)
cv2.destroyAllWindows()
