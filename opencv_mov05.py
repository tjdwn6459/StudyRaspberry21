
import cv2
import numpy as np
import datetime
from PIL import ImageFont, ImageDraw, Image


#카메라 기본 틀
# 영상에 글자 출력
cap = cv2.VideoCapture(0) #번호 0부터 +1
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640) #넓이와 높이 수동설정 (카메라가 가진 영상의 크기를 넣어야한다) 
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

#나눔고딕볼드 로드
font = ImageFont.truetype('./fonts/NanumGothicBold.ttf', 20) 

#무한루프(q를 입력할때까지)
while True:
    ret, frame = cap.read() #카메라 현재 영상 로드, frame 저장, ret True/False
    h, _, _ = frame.shape #Width,Channel은 필요 없기에 빈공간 
    now = datetime.datetime.now()
    currDateTime = now.strftime('%Y-%m-%d %H:%M:%S')

    if ret != True:break #ret이 False이면 탈출

    frame = Image.fromarray(frame)#글자출력을 위해 변환
    draw = ImageDraw.Draw(frame)
    draw.text(xy=(10, 50), text='실시간 웹캠 - {0}'.format(currDateTime),font=font, fill=(0, 0, 255))
    frame = np.array(frame) #원상태 복귀

    cv2.imshow('RealTime CAM', frame) # 로드한 영상을 창에 띄움
  
    if cv2.waitKey(1) == ord('q'): #q를 입력하면 루프 탈출!
        break

cap.release() #웹캠 해제
cv2.destroyAllWindows()