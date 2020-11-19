# 1. 저장소 Output 파일 생성 및 생성확인.
# 2. 영상 10초 분할 및 생성 날짜 기록.
# 3. 저장소 파일 용량 확인.
# 4. 저장소 파일 리스트.


import cv2
import numpy as np                  # 행렬이나 다차원배열 관련 파이썬라이브러리 함수.
import matplotlib.image as mpimg    # 이미지read 관련 함수.
import matplotlib.pyplot as plt     # 차트,플롯 관련 함수.
import os
import time
import datetime

from calibration import calib, undistort
from threshold import gradient_combine, hls_combine, comb_result
from finding_lines import Line, warp_image, find_LR_lines, draw_lane, print_road_status, print_road_map
from skimage import exposure

input_type = "video"                # 입력파일 형식.
input_name = "project_video.mp4"    # 입력파일 이름.

readpath = '/'
savepath = './output'
if savepath == None:          # Output파일 조건생성.
    os.mkdir('./output')
    print("저장 파일이 생성되었습니다.")
else:
    print("이미 폴더가 있습니다.\n")
    pass

left_line = Line()
right_line = Line()

th_sobelx, th_sobely, th_mag, th_dir = (35, 100), (30, 255), (30, 255), (0.7, 1.3)
th_h, th_l, th_s = (10, 100), (0, 60), (85, 255)

# camera matrix & distortion coefficient
mtx, dist = calib()

if input_type == 'video':

    cap = cv2.VideoCapture(input_name)

    fourcc = cv2.VideoWriter_fourcc(*'XVID') #비디오코덱 설정

    fps = cap.get(cv2.CAP_PROP_FPS) #영상의 fps값 가져오기.

    date_string = datetime.datetime.now().strftime("%Y-%m-%d  %I.%M.%S%p   %A")  # data 파일명 지정.

    date_path = os.path.join(savepath, date_string)  # 저장위치와 파일명을 결합.

    incnt = 0   #info2 카운터 값 초기화.
    innum = 0   #info2 파일번호 값 초기화.

    recnt = 0   #combined_result 카운터 값 초기화.
    renum = 0   #combined_result 파일번호 값 초기화.

    # out = cv2.VideoWriter('./'+date_string+'_[%i].avi' % recnt, fourcc, fps, (640, 128), 0)
    # out2 = cv2.VideoWriter('./output/' +date_string +'_[%i].avi' % incnt, fourcc, fps, (640, 360))

    while (cap.isOpened):
        _, frame = cap.read()

        # Correcting for Distortion
        undist_img = undistort(frame, mtx, dist)
        # resize video
        undist_img = cv2.resize(undist_img, None, fx=1 / 2, fy=1 / 2, interpolation=cv2.INTER_AREA)

        rows, cols = undist_img.shape[:2]

        combined_gradient = gradient_combine(undist_img, th_sobelx, th_sobely, th_mag, th_dir)
        #cv2.imshow('gradient combined image', combined_gradient)

        combined_hls = hls_combine(undist_img, th_h, th_l, th_s)
        #cv2.imshow('HLS combined image', combined_hls)

        combined_result = comb_result(combined_gradient, combined_hls)
        # width, height = combined_result.shape
        # print(combined_result.shape)
        # combined_result.shape의 가로, 세로 값 얻어오기.

        secfps = fps * 10  # fps * 초

        # combined_result의 영상분할 조건식. ./ 디렉토리에 저장.
        if (0 < recnt and recnt < secfps):  # 최초 이후 조건문을 적용, 프레임카운터에 의해 영상 분할.
            out.write(combined_result)
            recnt += 1
        elif recnt == 0:            # 최초 영상 분할 생성.
            out = cv2.VideoWriter(savepath + '_[%i].avi' % renum, fourcc, fps, (640, 128), 0)
            out.write(combined_result)
            recnt += 1
            renum += 1
        else:
            recnt = 0

        c_rows, c_cols = combined_result.shape
        s_LTop2, s_RTop2 = [c_cols / 2 - 24, 5], [c_cols / 2 + 24, 5]
        s_LBot2, s_RBot2 = [110, c_rows], [c_cols - 110, c_rows]

        src = np.float32([s_LBot2, s_LTop2, s_RTop2, s_RBot2])
        dst = np.float32([(170, 720), (170, 0), (550, 0), (550, 720)])

        warp_img, M, Minv = warp_image(combined_result, src, dst, (720, 720))
        #cv2.imshow('warp', warp_img)

        searching_img = find_LR_lines(warp_img, left_line, right_line)
        #cv2.imshow('LR searching', searching_img)

        w_comb_result, w_color_result = draw_lane(searching_img, left_line, right_line)
        #cv2.imshow('w_comb_result', w_comb_result)

        # Drawing the lines back down onto the road
        color_result = cv2.warpPerspective(w_color_result, Minv, (c_cols, c_rows))
        lane_color = np.zeros_like(undist_img)
        lane_color[220:rows - 12, 0:cols] = color_result
        # Combine the result with the original image

        result = cv2.addWeighted(undist_img, 1, lane_color, 0.3, 0)
        #cv2.imshow('result', result.astype(np.uint8))

        info, info2 = np.zeros_like(result),  np.zeros_like(result)
        info[5:110, 5:190] = (255, 255, 255)
        info2[5:110, cols-111:cols-6] = (255, 255, 255)
        info = cv2.addWeighted(result, 1, info, 0.2, 0)
        info2 = cv2.addWeighted(info, 1, info2, 0.2, 0)
        road_map = print_road_map(w_color_result, left_line, right_line)
        info2[10:105, cols-106:cols-11] = road_map
        info2 = print_road_status(info2, left_line, right_line)
        # cv2.imshow("info2", info2)
        # out = cv2.VideoWriter(date_path + '.avi', fourcc, fps, (int(width1), int(height1)))
        # info2 원본파일의 저장 위치
        # out.write(info2)
        # height1, width1 = info2.shape[:2]
        # 컬러의 경우 인자가 3개이므로 2개만 받아온다.

        if (0 < incnt and incnt < secfps):
            out2.write(info2)
            incnt += 1
        elif incnt == 0:
            out2 = cv2.VideoWriter('./output/' + date_string + '[%i].avi' % innum, fourcc, fps, (640, 360))
            out2.write(info2)
            incnt += 1
            innum += 1
        else:
            incnt = 0

        if cv2.waitKey(1) & 0xFF == ord('s'):
            cv2.waitKey(0)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()

out.release()
out2.release()


n = os.path.getsize(savepath)
m = os.listdir(savepath)
x = int(len(m))
print("저장소의 전체파일의 크기는")
print("Output :", n, "Bytes 입니다.\n")
print("저장소 파일 리스트")
i = 0
for i in m:
    print("file_list: {}".format(i))

