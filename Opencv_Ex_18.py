import numpy as np
import glob, cv2


criteria = (cv2.TERM_CRITERIA_EPS+cv2.TERM_CRITERIA_MAX_ITER, 30 ,0.001)

objp = np.zeros((7*9,3),np.float32)

objp[:,:2] = np.mgrid[0:7,0:9].T.reshape(-1,2)

objpoints = [] # 실제 세계의 3D 점들
imgpoints = [] # 2D 이미지의 점들

images = glob.glob('/home/ubuntu/Opencv/data/img_2/chess*.jpg')

for name in images:
    images = cv2.imread(name)
    size = (700, 700)
    dst = cv2.resize(images, dsize=size, interpolation=cv2.INTER_AREA)
    gray = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)

    ret, corners = cv2.findChessboardCorners(gray,(7,9),None)

    if ret == True:
        objpoints.append(objp)

        corners2 = cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
        imgpoints.append(corners2)

        dst = cv2.drawChessboardCorners(dst,(7,9),corners2,ret)
        cv2.imshow('img',dst)
        cv2.waitKey(2000)
        cv2.destroyAllWindows()