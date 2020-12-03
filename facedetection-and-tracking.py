import cv2
import os
dataset="dataset"
name="heath"
path=os.path.join(dataset,name)
#if folder not there then folder is created
if not os.path.isdir(path):
    os.mkdir(path)

(width,height)=(130,100)




alg="haarcascade_frontalface_default.xml"
haarcascade=cv2.CascadeClassifier(alg)
cam=cv2.VideoCapture(0)
c=1
while c<31:
    print(c)
    _,img=cam.read()

    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face=haarcascade.detectMultiScale(gray,1.3,4)
    for (x,y,w,h) in face:

        cv2.rectangle(img,(x,y),(x+w,y+h), (0,255,0),2)
        faceonly=gray[y:y+h,x:x+w]
        resizeimg=cv2.resize(faceonly,(width,height))
        cv2.imwrite("%s/%s.jpg" % (path,c),resizeimg)
        c=c+1

    cv2.imshow("FaceDetection",img)
    key=cv2.waitKey(1)&0xFF
    if key== ord("x"):
        break

print("imagecaptured")
cam.release()
cv2.destroyAllWindows()
