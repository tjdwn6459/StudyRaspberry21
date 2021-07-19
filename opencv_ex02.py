import cv2

#기본소스 opencv 소스 
cam = cv2.VideoCapture(0) #기본카메라
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 320) #창 넓이
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 240) # 창 높이

fourcc = cv2.VideoWriter_fourcc(*'XVID') #xvid 비디오 코텍
is_record = False # 녹화상태

while True:
    ret, frame = cam.read() #웹캠읽기
    frame = cv2.flip(frame, 0)


    if ret:
        cv2.imshow('CAM', frame) #카메라  영상  cam이라는 이름으로 창에 띄움

        key = cv2.waitKey(1)
        if key == ord('q'): #q를 입력받으면
           break
        elif key == ord('c'): #c를 입력 받으면
            cv2.imwrite('./capture/captured.jpg', frame)
            print('이미지 캡처 완료')
        elif key ==ord('r') and is_record == False: #r을 입력하면 레코딩
            is_record = True
            video = cv2.VideoWriter('./capture/record.avi', fourcc, 20, (frame.shape[1], frame.shape[0]))
            print('녹화시작')

        elif key == ord('r') and is_record == True: #녹화중 
            is_record = False
            video.release()
            print('녹화완료')

        if is_record == True: #현재회면 녹화
            video.write(frame)
cam.release()
cv2.destroyAllWindows()