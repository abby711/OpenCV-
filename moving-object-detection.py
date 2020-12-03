import cv2
import time
import imutils

cam=cv2.VideoCapture(0)
time.sleep(1)
firstframe=None
area=500
while True:
    _,img=cam.read()
    text="Normal"
    img=imutils.resize(img,width=500)
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    gaussian=cv2.GaussianBlur(gray,(21,21),0)
    if firstframe is None:
        firstframe=gaussian
        continue
    imgdiff=cv2.absdiff(firstframe,gray)#diff btwn new frame and frstframe
    threshimg=cv2.threshold(imgdiff,25,255,cv2.THRESH_BINARY)[1]
    threshimg=cv2.dilate(threshimg,None,iterations=2)
    cnts=cv2.findContours(threshimg.copy(),cv2.RETR_EXTERNAL,
                          cv2.CHAIN_APPROX_SIMPLE)
    cnts=imutils.grab_contours(cnts)
    for c in cnts:
        if cv2.contourArea(c)<area:
            continue
        (x,y,w,h)=cv2.boundingRect(c)
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        text="a moving object is detected"
        print(text)
    cv2.putText(img,text,(10,20),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)







    cv2.imshow("CAMERA-FEED",img)
    key=cv2.waitKey(1)&0xFF
    if key== ord("x"):
        break

#cv2.imwrite("background.jpg",img)
cam.release()
cv2.destroyAllWindows()
