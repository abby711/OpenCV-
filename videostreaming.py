#streaming=== reading and displying a video
#video is a collection of frames(images)
#only videomis played no audioooooooo
import cv2

video=cv2.VideoCapture('C:/Users/Abirami/OneDrive/Desktop/internship/beyonce.mp4')
#to capture video via webcam video.cv2.VideoCapture(0)
while(True):
    
    ret, frame=video.read()
    cv2.imshow('input video',frame)    #frames of the video are displayed simultaneously
    print('video streaming')
    if cv2.waitKey(1) & 0xFF ==ord('s'):
       break
video.release()
cv2.destroyAllWindows()
       
