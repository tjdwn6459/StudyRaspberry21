import cv2

#기본소스 opencv 소스 
cam = cv2.VideoCapture(0) #기본카메라
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 320) #창 넓이
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 240) # 창 높이

while True:
    ret, frame = cam.read() #웹캠읽기
    frame = cv2.flip(frame, 0)


    if ret:
        cv2.imshow('CAM', frame) #카메라  영상  cam이라는 이름으로 창에 띄움

        key = cv2.waitKey(1)
        if key == ord('q'): #q를 입력받으면
           break

cam.release()
cv2.destroyAllWindows()