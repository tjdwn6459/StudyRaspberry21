from typing import ChainMap
import cv2
import numpy as np


#카메라 기본 틀
cap = cv2.VideoCapture(0) #번호 0부터 +1
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320) #넓이와 높이 수동설정 (카메라가 가진 영상의 크기를 넣어야한다) 
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

#무한루프(q를 입력할때까지)
while True:
    ret, frame = cap.read() #카메라 현재 영상 로드, frame 저장, ret True/False
    
    if ret != True: break #ret이 False이면 루프 탈출

    h, w, c = frame.shape #영상하나의 높이, 넓이, 채널
    print('Width : {0}, Height : {1}, Channel : {2}'.format(w, h, c))

    cv2.imshow('RealTime CAM', frame) # 로드한 영상을 창에 띄움

    if cv2.waitKey(1) == ord('q'): #q를 입력하면 루프 탈출!
        break

cap.release()
cv2.destroyAllWindows()