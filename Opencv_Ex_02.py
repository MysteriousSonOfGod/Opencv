#이미지 압축/품질 조정.

import cv2

imageFile = './data/lena.jpg'

img = cv2.imread(imageFile)

cv2.imwrite('./data/Lena.bmp',img)      # jpg파일을 bmp파일로 이미지를 저장한다.

# cv2.imwrite('./data/Lena.png',img)    # jpg파일을 png파일로 이미지를 저장한다.
#
# cv2.imwrite('./data/Lena2.png', img, [cv2.IMWRITE_PNG_COMPRESSION, 9])   # png 이미지압축 9, 기본값 3

cv2.imwrite('./data/Lena2.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 50])       # jpeg 이미지품질 50%로 설정.

