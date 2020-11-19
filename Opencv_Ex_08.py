#이미지 Crop 중심을 기준으로 기준값으로 자름.

import cv2

path = "/home/ubuntu/Opencv/data/lena.jpg"
src = cv2.imread(path)

dst = src.copy()
dst = src[100:600, 200:700]

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()