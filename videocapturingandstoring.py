import cv2
video=cv2.VideoCapture(0) #capture video
framew=int(video.get(3))
frameh=int(video.get(4))
size=(framew,frameh)
#to store video
result=cv2.VideoWriter('out.avi',cv2.VideoWriter_fourcc(*'MJPG'),10, size)
while(True):
    ret,frame=video.read()
    result.write(frame)
    cv2.imshow('Frame',frame)
    if(cv2.waitKey(1) & 0xFF == ord('s')):
        break
print("the frame was successfullly saved")    
video.release() #stops capturing
result.release() #stop op video we got
cv2.destroyAllWindows()
           
 
    
