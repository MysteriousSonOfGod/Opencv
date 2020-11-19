import cv2
vidcap = cv2.VideoCapture('myvid.mp4')
success,image = vidcap.read()
count = 0;

# number of frames to skip
numFrameToSave = 10

print "I am in success"
while success: # check success here might break your program
     success,image = vidcap.read() #success might be false and image might be None
     #check success here
     if not success:
       break

     # on every numFrameToSave
     if (count % numFrameToSave ==0):
       cv2.imwrite("img_%3d.jpg" % count, image)

     if cv2.waitKey(10) == 27:
         break
     count += 1