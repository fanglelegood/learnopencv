import cv2 
import numpy as np

dog = cv2.imread('./dog.jpg')
cat = cv2.imread('./cat1.jpg')

print(dog.shape)
print(cat.shape)

result = cv2.addWeighted(dog, 0.8 , cat ,0.2 ,0)  #0是静态权重，就是生成后继续加亮
cv2.imshow('add2' , result)
cv2.waitKey(0)