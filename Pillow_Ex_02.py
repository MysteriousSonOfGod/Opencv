#Pillow를 이용하여 이미지 크기 조절 및 스냅샷 적용.

from PIL import Image

path = "/home/ubuntu/Opencv/data/lena.jpg"
print(path)

im = Image.open(path)
img2 = im.resize((800, 800))  #tuble값으로 데이터값을 넣어줌
img3 = im.crop((100, 100, 350, 350))
img2.show()
