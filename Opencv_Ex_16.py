#Opencv_MouseDrag
import cv2
import numpy as np

# Mouse Callback함수
def On_MouesDrag(event, x, y, flags, param):
    global pt1, pt2

    if event == cv2.EVENT_LBUTTONDOWN:  # 마우스를 누른 상태
        pt1 = (x, y) #클릭좌표

    elif event == cv2.EVENT_LBUTTONUP: # 마우스를 해제 상태
        pt2 = (x, y) #클릭해제 좌표
        cv2.rectangle(img, pt1, pt2, (0, 0, 255), 1)
        # RED값으로 두께 1 사각박스 지정.

        org = [0,0]
        #좌표값 비교문 클릭좌표와 해제좌표를 비교하여 좌표정보를 표기.
        if(pt1[0] > pt2[0]):
            org[0] = pt2[0]
            xLength = pt1[0] - pt2[0]
        elif (pt1[0] < pt2[0]):
            org[0] = pt1[0]
            xLength = pt2[0] - pt1[0]

        if (pt1[1] > pt2[1]):
            org[1] = pt2[1]
            yLength = pt1[1] - pt2[1]

        elif (pt1[1] < pt2[1]):
            org[1] = pt1[1]
            yLength = pt2[1] - pt1[1]

        text = 'X : '+str(pt1)+' Y : '+str(pt2)+' xLength' +str(xLength) +' yLength' + str(yLength)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, text, tuple(org), font, 0.8, (0, 0, 255), 1)

# 캔버스, MouseCallback 함수 설정
img = np.zeros((1028, 1028, 3), np.uint8) +255 #백색캔버스를 생성
cv2.namedWindow('image')
cv2.setMouseCallback('image', On_MouesDrag)  # 마우스 이벤트 후 callback 수행하는 함수 지정

# main문 : 키보드로 esc를 받을때까지 화면을 계속 보여준다.
while True:
    cv2.imshow('image', img)  # 화면을 보여준다.

    k = cv2.waitKey(1) & 0xFF  # 키보드 입력값을 받고

    if k == 27:  # esc를 누르면 종료
        break

cv2.destroyAllWindows()