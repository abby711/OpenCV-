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
import os
from playsound import playsound
#from gtts import gTTS #for google translator(not used here)

def lipdistance(s): #from the 68 landmarks of face
    toplip=s[50:53] #50-53 upper top lip landmark
    toplip=np.concatenate((toplip,s[61:64]))#appending with lower top lip landmark
    lowlip=s[56:53]
    lowlip=np.concatenate((lowlip,s[65:68]))
    topmean=np.mean(toplip, axis=0)#average point among all the points to rep toplip
    lowmean=np.mean(lowlip,axis=0)#average point for the lowerlip
    dis=abs(topmean[1]-lowmean[1])
    return dis


ap=argparse.ArgumentParser()
#ap.add_argument("-p","--shape-predictor", required=True, help="path to facial landmark predictor")
ap.add_argument("-w", "--webcam" , type=int ,default=0 ,help="index of webcam on system")
args=vars(ap.parse_args())
eyethresh=0.3
eyeframes=30




alarmstatus=False
alarmstatus2=False
saying=0
c=0
print("****loading predictor and detector")
detector=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
predictor=dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

print("-> Starting Video Stream")
vs = VideoStream(src=args["webcam"]).start()
#vs= VideoStream(usePiCamera=True).start()       //For Raspberry Pi
time.sleep(1.0)


while True:
    frame=vs.read()
    frame=imutils.resize(frame,width=400)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    rects= detector.detectMultiScale(gray, scaleFactor=1.1,
                                     minNeighbors=5, minSize=(30,30))
    for (x,y,w,h) in rects:
        rect=dlib.rectangle(int(x), int(y),int(x+w),int(y+h))
        shape=predictor(gray,rect)
        shape=face_utils.shape_to_np(shape)

    
        distance=round(lipdistance(shape))
        lip=shape[48:60]
        cv2.drawContours(frame,[lip],-1,(0,255,0),1)
        
        if(distance>16):
            cv2.putText(frame,"A",(10,30),
                        cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)
            print("A")
            
        elif(distance==4):
            cv2.putText(frame,"B",(10,30),
                        cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)
            print("B")
            
        elif(distance==12):
            cv2.putText(frame,"C",(10,30),
                        cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)
            print("C")
            
        elif(distance==8 or distance==9):
            cv2.putText(frame,"D",(10,30),
                        cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)
            print("D")
            
        else:
            alaramstatus2=False

        cv2.putText(frame,"lipdet:{:.2f}".format(distance),(300,30),
                     cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)
    cv2.imshow("Frame", frame)
    if(cv2.waitKey(1) & 0xFF == ord('s')):
                      break


cv2.destroyAllWindows()
vs.stop()    
                                     
