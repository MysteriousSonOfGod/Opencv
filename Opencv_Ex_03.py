#이미지 색상 변화.

import os
import cv2
from matplotlib import pyplot as plt

print("파일위치확인 :", os.path.isfile("/home/ubuntu/pythonProject/data/lena.jpg"))

imageFile = './data/lena.jpg'

imgBGR = cv2.imread(imageFile)

plt.axis('off')

imgRGB = cv2.cvtColor(imgBGR,cv2.COLOR_BGR2RGB)
plt.imshow(imgBGR)
plt.show()