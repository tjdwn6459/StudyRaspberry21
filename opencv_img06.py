import cv2
import numpy as np #c#의 리스트, 행렬이 포함되어 있지 않아, numpy

#이미지 로드 기본틀
## 이미지 대비
org = cv2.imread('./image/dog.jpg', cv2.IMREAD_REDUCED_COLOR_2)
gray = cv2.cvtColor(org, cv2.COLOR_BGR2GRAY)
enhanced = cv2.equalizeHist(gray)

cv2.imshow('original', org)#cv2로 새창이 열린다(이미지를 새창에 띄우기)
cv2.imshow('Gray', gray)
cv2.imshow('Enhance', enhanced)

cv2.waitKey(0) #이게 없으면 창이 열리고 바로 꺼진다 (창 키 입력 대기)
cv2.destroyAllWindows() #메모리 해제 