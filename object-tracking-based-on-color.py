import imutils
import cv2
#for yellow color
lower=(0,153,100)
upper=(179,255,255)
cam=cv2.VideoCapture(0)
while True:
    _,frame=cam.read()
    frame=imutils.resize(frame,width=600)
    gauss=cv2.GaussianBlur(frame,(11,11),0)
    hsv=cv2.cvtColor(gauss,cv2.COLOR_BGR2HSV)
    mask=cv2.inRange(hsv,lower,upper) #the area that is to bee masked
    mask=cv2.erode(mask,None,iterations=2) #removes any stuff over tat color images
    mask=cv2.dilate(mask,None,iterations=2)

    contor=cv2.findContours(mask.copy(),cv2.RETR_EXTERNAL,
         cv2.CHAIN_APPROX_SIMPLE)[-2]
    center=None
    if len(contor)>0:
        c=max(contor,key=cv2.contourArea)
        ((x,y),radius)=cv2.minEnclosingCircle(c)
        M=cv2.moments(c)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
        if radius >10:
            cv2.circle(frame,(int(x),int(y)),int(radius),(255,0,255),2)
            cv2.circle(frame,center,5,(0,0,255),-1)
            if radius>250:
                print("stop")
            else:
                if(center[0]<150):
                    print("left")
                elif(center[0]>450):
                    print("right")
                elif(radius<250):
                    print("front")
                else:
                    print("stop")
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("x"):
                break

cam.release()
cv2.destroyAllWindows()
