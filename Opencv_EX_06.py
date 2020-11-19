import sys
import numpy as np
import cv2

src = cv2.imread('/home/ubuntu/Opencv/data/building.jpg', cv2.IMREAD_GRAYSCALE)
dst = cv2.GaussianBlur(src, (3, 3), 0)  # 노이즈 제거
ost = cv2.Canny(dst, 50, 150)

if src is None:
    print('Image load failed!')
    sys.exit()

x_dst, y_dst = 0,0
def onChange(pos): # 트랙바 핸들러
    global x_dst, y_dst
    dst1 = cv2.setTrackbarPos(src, x_dst, y_dst)
    dst2 = cv2.setTrackbarPos(src, x_dst, y_dst)
    ost = cv2.Canny(src, dst1, dst2)

cv2.imshow('Canny', ost)
# 트랙바 생성
cv2.createTrackbar('dst1', 'Canny', 0, 255, onChange) # x값의 트랙바 최소값,최대값
cv2.createTrackbar('dst2', 'Canny', 0, 255, onChange) # y값의 트액바 최소값,최대값
# 트랙바 위치 초기화
cv2.setTrackbarPos('dst1', 'Canny', 50)  # x 트랙바의 기본 시작값
cv2.setTrackbarPos('dst2', 'Canny', 150) # y 트랙바의 기본 시작값


cv2.waitKey()
cv2.destroyAllWindows()
