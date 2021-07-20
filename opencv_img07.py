import cv2
import numpy as np #c#의 리스트, 행렬이 포함되어 있지 않아, numpy

#이미지 로드 기본틀
## 영상둘레표시 컨투어(윤곽)
org = cv2.imread('./image/dog.jpg', cv2.IMREAD_REDUCED_COLOR_2)
gray = cv2.cvtColor(org, cv2.COLOR_BGR2GRAY)
ret, bny = cv2.threshold(gray, 127, 255, 0)
cont, hirc = cv2.findContours(bny, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(org, cont, -1, (255, 0, 0), 1)
cv2.drawContours(org, cont, 0, (0, 255, 0), 2 )
cv2.imshow('Result', org)

cv2.waitKey(0) #이게 없으면 창이 열리고 바로 꺼진다 (창 키 입력 대기)
cv2.destroyAllWindows() #메모리 해제 