#이미지 window창으로 오픈.

import cv2

imageFile = './data/lena.jpg'   # 이미지파일위치

img = cv2.imread(imageFile)     # 이미지파일의 지정된 이미지를 읽고 img 저장.

img2 = cv2.imread(imageFile,0)

cv2.imshow('Lena color', img)   # 이미지 출력 (이미지창이름, 함수명)

cv2.imshow('Lena grayscale', img2) # 이미지 출력 (이미지창이름, 함수명)

cv2.waitKey()                   # 이미지 출력 시 종료키를 설정, 없을시 창이 바로 종료된다.
cv2.destroyAllWindows()         # 출력 시 종료 버튼을 생성.

