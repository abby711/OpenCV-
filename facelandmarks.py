import cv2
import numpy as np
import dlib #for face realted stuff particullary face landmarks
#we are using unsupervised here so deeplearning
import winsound
freq=500
dur=2000
cap = cv2.VideoCapture(0)
detect=dlib.get_frontal_face_detector() #initilisating detector has front face info
predict=dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
while True:
    _,frame=cap.read()
    cv2.imshow('input frame',frame)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=detect(gray)
       
    for face in faces: #for multiple faces
        #landmark code starts
        x1=face.left()
        y1=face.top()
        x2=face.right()
        y2=face.bottom()

        landmarks=predict(gray,face)
        print("landmark collected!!")
        cv2.putText(frame,"face landmarks detected",(10,30),cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,(0,0,255),2)
        for n in range(0,68): #68 landmarks arethere
            x=landmarks.part(n).x
            y=landmarks.part(y).y
            cv2.circle(frame,(x,y),2,(255,255,0),-1)
                              #center position,radius,color,to fill the color(-1)
  
    cv2.imshow('result',frame)
    k = cv2.waitKey(30) & 0xff
    if k == 27: 
        break
  

cap.release() 
  
 
cv2.destroyAllWindows()
            
            
        
