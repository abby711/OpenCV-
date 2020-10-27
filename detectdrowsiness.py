from scipy.spatial import distance as dist
from imutils.video import VideoStream
from imutils import face_utils
from threading import Thread
import numpy as np
import winsound
fre=400
dur=2000
import argparse
import imutils
import time
import dlib
import cv2

def eye_aspect_ratio(e):
    A=dist.euclidean(e[1],e[5])
    B=dist.euclidean(e[2],e[4])
    C=dist.euclidean(e[0],e[3])
    ear=(A+B)/(2.0*C)
    return ear

ap=argparse.ArgumentParser()
ap.add_argument("-p","--shape-predictor", required=True, help="path to facial landmark predictor")
ap.add_argument("-w", "--webcam" , type=int ,default=0 ,help="index of webcam on system")
args=vars(ap.parse_args())

eyeth=0.25
eyeframes=10
c=0

print("********* loading facial landmark")
detector=dlib.get_frontal_face_detector()
predictor=dlib.shape_predictor(args["shape_predictor"])

(lstart,lend)=face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
(rstart,rend)=face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]
print("********* staring video stream thread")


cap=cv2.VideoCapture(0)
while True:
    ret,frm=cap.read()
    cv2.imshow('frame',frm)
    frame=imutils.resize(frm,width=800)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    rects=detector(gray,0)
    for rect in rects:
        shape=predictor(gray,rect)
        shape=face_utils.shape_to_np(shape)
        lefteye=shape[lstart:lend]
        righteye=shape[rstart:rend]
        leftear=eye_aspect_ratio(lefteye)
        rightear=eye_aspect_ratio(righteye)
        ear=(leftear+rightear)/2.0
        lefteyehull=cv2.convexHull(lefteye)
        righteyehull=cv2.convexHull(righteye)
        cv2.drawContours(frame,[lefteyehull],-1,(0,255,0),1)
        cv2.drawContours(frame,[righteyehull],-1,(0,255,0),1)
        if ear < eyeth :
            c+=1
            if c >= eyeframes:
                cv2.putText(frm,"DROWSINESS ALERT!",(10,30),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)
            winsound.Beep(fre,dur)
        else:
                c=0
        cv2.putText(frame,"EAR:{:.2f}".format(ear),(300,30),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)
    cv2.imshow("Frame", frame)
    if(cv2.waitKey(1) & 0xFF == ord('s')):
        break


cv2.destroyAllWindows()
vs.stop()
        

                                                                                          


        
