#access video from ipwebcame via phone and to just display it
import urllib.request
import cv2
import numpy as np
import time
#replace the url with ipwebcam shot.jpg IP:port
url=' http://192.168.1.3:8080/shot.jpg'
while True:
    imgresp=urllib.request.urlopen(url) #get image from webcam
    imgnp=np.array(bytearray(imgresp.read()),dtype=np.uint8) #convert into array
    img=cv2.imdecode(imgnp,-1)
    img=cv2.resize(img,(800,800))
    cv2.imshow('IPWEBCAM',img)
    if(cv2.waitKey(1) & 0xFF == ord('s')):
        break
   

cv2.destroyAllWindows()
