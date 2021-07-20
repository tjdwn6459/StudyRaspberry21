import cv2
import numpy as np #c#의 리스트, 행렬이 포함되어 있지 않아, numpy

#이미지 로드 기본틀
## 노이즈 추가
org = cv2.imread('./image/dog.jpg', cv2.IMREAD_REDUCED_COLOR_2)
h, w, c = org.shape
noise = np.uint8(np.random.normal(loc=0, scale=80.0, size=[h, w, c]))
noised_img = cv2.add(org, noise)

cv2.imshow('original', org)#cv2로 새창이 열린다(이미지를 새창에 띄우기)
cv2.imshow('Noise', noised_img)

cv2.waitKey(0) #이게 없으면 창이 열리고 바로 꺼진다 (창 키 입력 대기)
cv2.destroyAllWindows() #메모리 해제 