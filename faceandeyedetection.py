import cv2
import winsound
fre=400
dur=2000
face_cascade=cv2.CascadeClassifier('‪haarcascade_frontalface_default.xml')
eye_cascade=cv2.CascadeClassifier('haarcascade_eye.xml')
cap=cv2.VideoCapture(0)
while 1:
    ret,img=cap.read()
    cv2.imshow('color output',img)
    #converting to color for more easy detection
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cv2.imshow('gray output',gray)
    
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    #1.3= feature matching point 5=kernel
    #xywh=x,y,width,height
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
#(255,255,0)==>cyan color 2,thickness of box in display
        roigray=gray[y:y+h, x:x+w]
        roicolor=img[y:y+h, x:x+w]
        cv2.putText(img,'face detected',(20,20),cv2.FONT_HERSHEY_SIMPLEX,1, (0,0,255), 2, cv2.LINE_AA)
        print("ALERT!!!!!! FACE DETECTED")
        cv2.imwrite('face.jpg',img)
        eyes=eye_cascade.detectMultiScale(roigray)
        for (ex,ey,ew,eh) in eyes: 
            cv2.rectangle(roicolor,(ex,ey),(ex+ew,ey+eh),(0,127,255),2)
            cv2.putText(roi_color, 'eyes detected',(20,20),cv2.FONT_HERSHEY_SIMPLEX, 
				1, (0,255,255), 2, cv2.LINE_AA)
  
    # Display an image in a window 
    cv2.imshow('img',img) 
  
    # Wait for Esc key to stop 
    k = cv2.waitKey(30) & 0xff
    if k == 27: 
        break
  
# Close the window 
cap.release() 
  
# De-allocate any associated memory usage 
cv2.destroyAllWindows()
