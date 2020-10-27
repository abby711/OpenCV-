import urllib.request
import cv2
import numpy as np
import time
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') 


url=' ip webcam app's http url.shot.jpg'
while True:
    imgresp=urllib.request.urlopen(url) #get image from webcam
    imgnp=np.array(bytearray(imgresp.read()),dtype=np.uint8) #convert into array
    img=cv2.imdecode(imgnp,-1)
    img=cv2.resize(img,(800,800))
    cv2.imshow('IPWEBCAM',img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #cv2.imshow('gray output',gray)
  
    
    faces = face_cascade.detectMultiScale(gray, 1.3, 5) 
  
    for (x,y,w,h) in faces: 
          
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)  
        roi_gray = gray[y:y+h, x:x+w] 
        roi_color = img[y:y+h, x:x+w]
        cv2.putText(img, 'face detected',(20,20),cv2.FONT_HERSHEY_SIMPLEX, 
				1, (0,0,255), 2, cv2.LINE_AA)
        print("Alert! face detected")
        
        cv2.imwrite('face.jpg',img)
  
        
        eyes = eye_cascade.detectMultiScale(roi_gray)  
  
         
        for (ex,ey,ew,eh) in eyes: 
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,127,255),2)
            cv2.putText(roi_color, 'eyes detected',(20,20),cv2.FONT_HERSHEY_SIMPLEX, 
				1, (0,255,255), 2, cv2.LINE_AA)
  
     
    cv2.imshow('img',img) 
    if(cv2.waitKey(1) & 0xFF == ord('s')):
        break
   

cv2.destroyAllWindows()
