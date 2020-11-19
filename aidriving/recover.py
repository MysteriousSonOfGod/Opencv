# import cv2
# import glob
# import shutil  # 파이썬 파일 연산 함수.
# import numpy as np  # 행렬이나 다차원배열 관련 파이썬라이브러리 함수.
# import matplotlib.image as mpimg  # 이미지read 관련 함수.
# import matplotlib.pyplot as plt  # 차트,플롯 관련 함수.
# import os
#
# from calibration import calib, undistort
# from threshold import gradient_combine, hls_combine, comb_result
# from finding_lines import Line, warp_image, find_LR_lines, draw_lane, print_road_status, print_road_map, writeVideo
# from skimage import exposure
#
# input_type = "video"  # 입력파일 형식.
# input_name = "project_video.mp4"  # 입력파일 이름.
#
# readpath = '/'
# savepath = './output'
# if savepath == None:  # Output파일 조건생성.
#     os.mkdir('./output')
#     print("저장 파일이 생성되었습니다.")
# else:
#     print("이미 파일이 있습니다.")
#     pass
#
# left_line = Line()
# right_line = Line()
#
# th_sobelx, th_sobely, th_mag, th_dir = (35, 100), (30, 255), (30, 255), (0.7, 1.3)
# th_h, th_l, th_s = (10, 100), (0, 60), (85, 255)
#
# # camera matrix & distortion coefficient
# mtx, dist = calib()
#
# if input_type == 'video':
#     cap = cv2.VideoCapture(input_name)
#     while (cap.isOpened()):
#         _, frame = cap.read()
#
#         # Correcting for Distortion
#         undist_img = undistort(frame, mtx, dist)
#         # resize video
#         undist_img = cv2.resize(undist_img, None, fx=1 / 2, fy=1 / 2, interpolation=cv2.INTER_AREA)
#         rows, cols = undist_img.shape[:2]
#
#         combined_gradient = gradient_combine(undist_img, th_sobelx, th_sobely, th_mag, th_dir)
#         # cv2.imshow('gradient combined image', combined_gradient)
#
#         combined_hls = hls_combine(undist_img, th_h, th_l, th_s)
#         # cv2.imshow('HLS combined image', combined_hls)
#
#         combined_result = comb_result(combined_gradient, combined_hls)
#         cv2.imshow('HLS combined image', combined_result)
#
#         c_rows, c_cols = combined_result.shape[:2]
#         s_LTop2, s_RTop2 = [c_cols / 2 - 24, 5], [c_cols / 2 + 24, 5]
#         s_LBot2, s_RBot2 = [110, c_rows], [c_cols - 110, c_rows]
#
#         src = np.float32([s_LBot2, s_LTop2, s_RTop2, s_RBot2])
#         dst = np.float32([(170, 720), (170, 0), (550, 0), (550, 720)])
#
#         warp_img, M, Minv = warp_image(combined_result, src, dst, (720, 720))
#         # cv2.imshow('warp', warp_img)
#
#         searching_img = find_LR_lines(warp_img, left_line, right_line)
#         # cv2.imshow('LR searching', searching_img)
#
#         w_comb_result, w_color_result = draw_lane(searching_img, left_line, right_line)
#         # cv2.imshow('w_comb_result', w_comb_result)
#
#         # Drawing the lines back down onto the road
#         color_result = cv2.warpPerspective(w_color_result, Minv, (c_cols, c_rows))
#         lane_color = np.zeros_like(undist_img)
#         lane_color[220:rows - 12, 0:cols] = color_result
#
#         # Combine the result with the original image
#         result = cv2.addWeighted(undist_img, 1, lane_color, 0.3, 0)
#         # cv2.imshow('result', result.astype(np.uint8))
#
#         info, info2 = np.zeros_like(result), np.zeros_like(result)
#         info[5:110, 5:190] = (255, 255, 255)
#         info2[5:110, cols - 111:cols - 6] = (255, 255, 255)
#         info = cv2.addWeighted(result, 1, info, 0.2, 0)
#         info2 = cv2.addWeighted(info, 1, info2, 0.2, 0)
#         road_map = print_road_map(w_color_result, left_line, right_line)
#         info2[10:105, cols - 106:cols - 11] = road_map
#         info2 = print_road_status(info2, left_line, right_line)
#         cv2.imshow('road info', info2)
#
#         if cv2.waitKey(1) & 0xFF == ord('s'):
#             cv2.waitKey(0)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

