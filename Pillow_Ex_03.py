#Pillow를 이용하여 이미지 블로우 넣기.

from PIL import Image, ImageFilter

path = "/home/ubuntu/Opencv/data/lena.jpg"
print(path)

im = Image.open(path)
img2 = im.filter((ImageFilter.BlUR))  #tuble값으로 데이터값을 넣어줌
img2.show()
