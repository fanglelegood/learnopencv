import cv2

fourcc = cv2.VideoWriter_fourcc('D', 'I', 'V', 'X')
vw = cv2.VideoWriter('out.avi', fourcc, 24, (640 ,480))

cv2.namedWindow('video', cv2.WINDOW_NORMAL)
cv2.resizeWindow('video', 640, 480)

cap = cv2.VideoCapture(0)
# cap = cv2.VideoCapture("D:\Camera外婆\VID_20211220_100130.mp4")


while cap.isOpened():
    ret, frame = cap.read()
    # width = int(frame.get(cv2.CAP_PROP_FRAME_WIDTH))
    # height = int(frame.get(cv2.CAP_PROP_FRAME_HEIGHT))
    # print("width:",width, "height:", height)
    print(frame.shape)
    if ret:
        cv2.imshow('video', frame)
        cv2.resizeWindow('video', 640, 480)
        
        vw.write(frame)
        key = cv2.waitKey(1)

        if (key & 0xFF == ord('q')):
            break
    else:
        break
cap.release()
vw.release()
cv2.destroyAllWindows()
