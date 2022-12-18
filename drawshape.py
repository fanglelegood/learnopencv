#功能
#画线，按下L 鼠标画线
#画矩形 按下R画矩形
#画圆 按C键

import cv2
import numpy as np

img = np.zeros((480, 640, 3), np.uint8)

curshape = 0
startpos = (0,0)

def mouse_callback(event, x, y, flags, userdata):
    # print(event, x, y, flags, userdata)
    global curshape ,startpos
    if (event& cv2.EVENT_LBUTTONDOWN == cv2.EVENT_LBUTTONDOWN):
        startpos = (x,y)
    elif (event& cv2.EVENT_LBUTTONUP == cv2.EVENT_LBUTTONUP):
        if curshape == 0:
            cv2.line(img, startpos, (x,y), (0,0,255))
        elif curshape == 1:
            cv2.rectangle(img, startpos, (x,y), (0,0,255))
        elif curshape == 2:
            a = (x- startpos[0])
            b = (y- startpos[1])
            r = int((a**2+b**2)**0.5)
            cv2.circle(img, startpos, r, (0,0,255))
        else:
            print('error:no shape')


cv2.namedWindow('drawshape', cv2.WINDOW_NORMAL)

#设置鼠标回调函数
cv2.setMouseCallback('drawshape', mouse_callback)

while True:
    cv2.imshow('drawshape', img)
    key = cv2.waitKey(1) & 0xFF
    if key  == ord('q'):
        break
    elif key == ord('l'):
        curshape = 0
    elif key == ord('r'):
        curshape = 1
    elif key == ord('c'):
        curshape = 2
cv2.destroyAllWindows()