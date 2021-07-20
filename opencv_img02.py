import cv2
import numpy as np #c#의 리스트, 행렬이 포함되어 있지 않아, numpy

#이미지 로드 기본틀
org = cv2.imread('./image/dog.jpg', cv2.IMREAD_REDUCED_COLOR_2) #흑백으로 로드(IMREAD_REDUCED_COLOR_2)사진을 반으로 줄인다)
gray = cv2.cvtColor(org, cv2.COLOR_BGR2GRAY)


h, w, c = org.shape
print('Width:{0}, Height:{1}, Channel:{2}'.format(w, h, c))
size_small = cv2.resize(org, dsize=(int(w/2), int(h/2))) #넓이와 높이를 반으로 줄인다(값이 float이 되기에 int 로 형변환) 

cv2.imshow('Original', org)#cv2로 새창이 열린다(이미지를 새창에 띄우기)
cv2.imshow('Gray', gray)
cv2.imshow('Resize', size_small) #이미지를 반으로 줄임 

cv2.waitKey(0) #이게 없으면 창이 열리고 바로 꺼진다 (창 키 입력 대기)
cv2.destroyAllWindows() #메모리 해제 