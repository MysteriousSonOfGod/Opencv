#이미지 채널을 생성하고 각 채널별 색상강조 적색, 녹색, 청색 하이라이트.

import cv2
import os
import numpy as np

path = "/home/ubuntu/Opencv/data/lena.jpg"

if os.path.isfile(path):
    src = cv2.imread(path)
    print("파일확인\n")
else:
    print("찾는 파일이 없습니다.\n")

b, g, r = cv2.split(src)
#이미지채널 분리, 분리된 채널은 단일 채널로 흑백의 색상만 표현한다.

height, width, channel = src.shape
print(height, width, channel)

zero = np.zeros((height, width, 1), dtype=np.uint8)
print(zero.shape)

imgB = cv2.merge((b, zero, zero))
imgG = cv2.merge((zero, g, zero))
imgR = cv2.merge((zero, zero, r))

cv2.imshow("BLUE", imgB)
cv2.imshow("GREEN", imgG)
cv2.imshow("RED", imgR)

cv2.waitKey()
cv2.destroyAllWindows()