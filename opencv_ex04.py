import cv2
import numpy as np
from numpy.core.defchararray import center


org = cv2.imread('./image/dog.jpg') #이미지 로드
dst = cv2.resize(org, dsize=(640, 840))

center = (250, 250) # x, y
color = (0, 0, 255) #red

cv2.rectangle(dst, (100, 100), (500, 300), (255, 0, 0)) #사각형
cv2.circle(dst, tuple(center), 30, color) #원
cv2.imshow("dest", dst)    #이미지창 띄우기


cv2.waitKey(0) #키 대기
cv2.destroyAllWindows() #opencv 인스턴스 종료 