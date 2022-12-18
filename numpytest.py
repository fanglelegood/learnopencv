import numpy as np
import cv2

img = np.zeros((480,640,3), np.uint8)

#改一根线颜色
# print(img[100,100])
# count = 0
# while count <200:
#     img[count, 100, 1] = 255
#     # img[count, 100] = [255 ,255 ,255]
#     count += 1

roi = img[100:200, 100:200]
roi[:,:] = [0,0,255]
roi[10:30, 20:50] = [0,255,0]

cv2.imshow('img', img)
key = cv2.waitKey(0)
if key & 0xFF == ord('q'):
    cv2.destroyWindow('img')



# a = np.array([1,2,3])

# b = np.array([[1,2,3],[4,5,6]])

# print(a)

# print(b)

# #定义zeros 矩阵
# c = np.zeros((8,8,3), np.uint8)
# print(c)

# d = np.ones((8,8), np.uint8)
# print(d)

# e = np.full((8,8), 255, np.uint8) 
# print(e)

# #定义单元举证
# f = np.identity(4)
# print(f)

# g = np.eye(5 ,7 , k=2)
# print(g)