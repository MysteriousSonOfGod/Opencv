#이미지 회전.

import cv2

path = "/home/ubuntu/Opencv/data/lena.jpg"
src = cv2.imread(path)
height, width, channel = src.shape
# 회전 중심, 회전각, scale
matrix = cv2.getRotationMatrix2D((width/2, height/2), 45, 1)
dst = cv2.warpAffine(src, matrix, (width, height))

cv2.imshow("src", src)
cv2.imshow("dst", dst)

cv2.waitKey()
cv2.destroyAllWindows()