import cv2
import numpy as np

min_w = 120 
min_h = 120
#检测线的高度
line_high = 520

#线的偏移
offset = 20

#储存有效车辆的数组
cars = []
#统计走过的车辆
carno = 0

def center(x ,y, w, h):
    x1= int(w/2)
    y1= int(h/2)    
    cx = x +x1
    cy = y +y1
    return cx, cy


#加载视频
cap = cv2.VideoCapture('test_1.mp4')

#去除背景
bgsubmog = cv2.bgsegm.createBackgroundSubtractorMOG()  #去除背景的api 后面要apply才可以

#形态学kernel
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))  #正方形腐蚀


while True:
    ret, frame = cap.read()

    if(ret == True):

        #灰度化
        cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #高斯滤波
        blur = cv2.GaussianBlur(frame, (3, 3), 5)
        #去除背景
        mask = bgsubmog.apply(blur)

        #腐蚀，去掉图中的小方块
        erode  = cv2.erode(mask, kernel)

        #膨胀（腐蚀后需要膨胀）还原
        dilate = cv2.dilate(erode, kernel, iterations=2)
        #闭操作 去掉物体内部的小方块
        close = cv2.morphologyEx(dilate, cv2.MORPH_CLOSE, kernel)
        close = cv2.morphologyEx(close, cv2.MORPH_CLOSE, kernel)

        #获取轮廓
        contours, hierarchy = cv2.findContours(close, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        #画一条检测线
        cv2.line(frame, (10,line_high), (1270, line_high), (255, 0, 0), 2)

        #画出轮廓方框
        for cnt in contours:
            (x,y,w,h) = cv2.boundingRect(cnt)
            
            #对轮廓的宽高做出判断
            isValid = ( w>= min_w ) and ( h>= min_h )

            if (not isValid):
                continue
            cv2.rectangle(frame, (x,y), (x+w, y+h), (255,255,0), 3)
            cpoint = center(x, y, w, h)
            cars.append(cpoint)
            for (x,y) in cars:
                #要有一条线
                #有范围
                #
                if(( y >line_high- offset ) and ( y< line_high +offset)):
                    carno += 1
                    cars.remove((x,y))
                    print(carno)
             
        cv2.imshow('frame', frame)
        # cv2.imshow('close', close)


    key = cv2.waitKey(33)
    if (key == 	27):
        break
cap.release()
cv2.destroyAllWindows()