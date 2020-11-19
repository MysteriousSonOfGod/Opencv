#이미지 채널을 나누고 회색조 단계별 이미지출력.

import cv2
import os

path = "/home/ubuntu/Opencv/data/lena.jpg"

if os.path.isfile(path):
    src = cv2.imread(path)
else:
    print("찾는 파일이 없습니다.")
b, g, r = cv2.split(src)

imgRGB = cv2.merge((b, g, r))

cv2.imshow("b",b)
cv2.imshow("g",g)
cv2.imshow("r",r)

cv2.imshow("imgRGB",imgRGB)

cv2.waitKey()
cv2.destroyAllWindows()
