#Pillow 사용하여 이미지 크기 조절.

from PIL import Image

path = "/home/ubuntu/Opencv/data/lena.jpg"

im = Image.open(path)

size =(64,64)

im.thumbnail(size)

print(im.size)

im.show()
outpath = "/home/ubuntu/Opencv/data/lena.jpg"
im.save(outpath)