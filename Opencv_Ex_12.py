# 0211.py
import matplotlib.pyplot as plt
import cv2, pafy

url = 'https://www.youtube.com/watch?v=u_Q7Dkl7AIk'
video = pafy.new(url)
print('title = ', video.title)
print('video.rating = ', video.rating)
print('video.duration = ', video.duration)

best = video.getbest(preftype='mp4')     # 'mp4','3gp'
print('best.resolution', best.resolution)

cap=cv2.VideoCapture(best.url)
#1
def handle_key_press(event):
    if event.key == 'escape':
        cap.release()
        plt.close()
def handle_close(evt):
    print('Close figure!')
    cap.release()

#2 프로그램 시작
# cap = cv2.VideoCapture() # 0번 카메라
plt.ion() # 대화모드 설정
fig = plt.figure(figsize=(10, 6)) # fig.set_size_inches(10, 6)
plt.axis('off')
#ax = fig.gca()
#ax.set_axis_off()
fig.canvas.set_window_title('Video Capture')        #타이틀이름
fig.canvas.mpl_connect('key_press_event', handle_key_press) #키호출하여 종료한다.
fig.canvas.mpl_connect('close_event', handle_close) #종료이벤트 등록 이미지가 종료되었을때 작동.

retval, frame = cap.read() # 첫 프레임 캡처
im = plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

#3
while True:
    retval, frame = cap.read() # 프레임 캡처
    if not retval:
        break
#    plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    im.set_array(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    fig.canvas.draw()               #
#   fig.canvas.draw_idle()
    fig.canvas.flush_events()  # plt.pause(0.001)
if cap.isOpened():
    cap.release()
