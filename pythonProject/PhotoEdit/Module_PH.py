import cv2
import os
import glob
from matplotlib import pyplot as plt

path = "/home/ubuntu/Opencv/dogs"
savepath = "/home/ubuntu/Opencv/dogs_test"

print("값을 입력하세요 : 크기편집 : [], 회전 : [], 블러 : [], 크롭 : []\n값은 1 또는 0 으로 입력하세요.")
s = input("").split()

list = dict(zip(range(len(s)), s))

if os.path.isdir(path):
    readdir = glob.glob(path+'/*.jpg')
    print("정상 : 파일 위치 확인.")
else:
    print("찾는 파일이 없습니다.\n")

if os.path.isdir(savepath):
    print("정상 : 저장파일 위치 확인.\n")
else:
    print("저장 디렉토리가 없습니다.\n")

class Editer():

    def Resize(self,img):
        x = list.get(0)
        src = img
        if x == 1:
            size = (400, 400)
            dst = cv2.resize(src, dsize=size, interpolation=cv2.INTER_AREA)
            return dst
        elif x == 0:
            dst = src
            return dst

    def Rotate(self,img):
        x = list.get(1)
        src = img
        if x == 1:
            height, width, channel = src.shape
            matrix = cv2.getRotationMatrix2D((width / 2, height / 2), 45, 1)
            dst = cv2.warpAffine(src, matrix, (width, height))
            return dst
        elif x == 0:
            dst = src
            return dst
    #
    # def Blur(self,img):
    #     x = list.get(2)
    #     print(x)
    #     src = img
    #     if x == 1:
    #         dst = cv2.blur(src, (4, 4), anchor=(-1, -1), borderType=cv2.BORDER_DEFAULT)
    #         return dst
    #
    # def Crop(self,img):
    #     x = list.get(3)
    #     print(x)
    #     src = img
    #     if x == 1:
    #         dst = src[10:10, 20:20]
    #         return dst
    #

cnt = 0

actResize = list.get(0)
actRotate = list.get(1)
actBlur = list.get(2)
actCrop = list.get(3)

Editer = Editer()
for image in readdir:

    img = cv2.imread(image)
    src = img
    print(src)

    if actResize:
        dst = Editer.Resize(src)


    elif actRotate:
        dst = Editer.Rotate(src)

    # elif list.get(2):
    #     img =Editer.Blur(src)
    #
    # elif list.get(3):
    #     img = Editer.Crop(src)


    savename = "img_%i"%cnt +".jpg"
    savepoint = os.path.join(savepath,savename)
    print()
    cv2.imwrite(savepoint, dst)
    cnt += 1

cv2.imshow("After Edit", src)
cv2.waitKey(2000)
cv2.destroyAllWindows()