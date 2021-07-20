import cv2
import numpy as np #c#의 리스트, 행렬이 포함되어 있지 않아, numpy

#이미지 로드 기본틀
## 이미지 흐르게 하기(Blur 블러)
org = cv2.imread('./image/dog.jpg', cv2.IMREAD_REDUCED_COLOR_2)
gray = cv2.cvtColor(org, cv2.COLOR_BGR2GRAY) #회색이미지
blur = cv2.blur(org, (10, 10))
kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
sharp = cv2.filter2D(org, -1, kernel)


cv2.imshow('original', org)#cv2로 새창이 열린다(이미지를 새창에 띄우기)
cv2.imshow('Blur',blur ) #흐리게 변경한 이미지
cv2.imshow('Sharp', sharp) #선명하게 


cv2.waitKey(0) #이게 없으면 창이 열리고 바로 꺼진다 (창 키 입력 대기)
cv2.destroyAllWindows() #메모리 해제 