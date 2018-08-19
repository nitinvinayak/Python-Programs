import numpy as np
import cv2
import matplotlib.pyplot as plt

img=cv2.imread('clicked.jpg')
cam=cv2.VideoCapture(0)

#gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#gray=np.float32(gray)
while True:
    ret,frame=cam.read()
    
    #cv2.imshow('frame',frame)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    gray=np.float32(gray)
    cv2.imshow('gray',gray)
    #print(gray)
    corners=cv2.goodFeaturesToTrack(gray,10,0.01,10)
    print(corners)
    print("DLIASJLDJLSAJDLJSLAJL")
    corners=np.int0(corners)
    print(corners)
    for corner in corners:
        x,y=corner.ravel()
        #print(corner)
        cv2.circle(frame,(x,y),4,255,-1)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
    
#cv2.imshow('IMG',img)
#cv2.waitKey(0)
cam.release()
cv2.destroyAllWindows()

