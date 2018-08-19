import cv2
import numpy as np

cam=cv2.VideoCapture(0)

while True:
    ret,frame=cam.read()
    #hue,saturation, value
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lower=np.array([150,100,0])
    upper=np.array([255,255,255])
    #For converting color from bgr to hsv
    #green = np.uint8([[[0,255,0 ]]])
    #hsv_green = cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
    #Now you take [H-10, 100,100] and [H+10, 255, 255] as lower bound and upper bound respectively.
    mask=cv2.inRange(hsv,lower,upper)
    res=cv2.bitwise_and(frame,frame,mask=mask)

    kernel=np.ones((15,15),np.float32)/225

    smooth=cv2.filter2D(res,-1,kernel)

    blur=cv2.GaussianBlur(res,(15,15),0)
    median=cv2.medianBlur(res,15)
    bilateral=cv2.bilateralFilter(res,15,100,100)
    
    cv2.imshow('frame',frame)
    cv2.imshow('res',res)
    #cv2.imshow('mask',mask)
    #cv2.imshow('smooth',smooth)
    cv2.imshow('MEDIAN',median)
    cv2.imshow('BLUR',blur)
    cv2.imshow('bilateral',bilateral)


    k=cv2.waitKey(1) & 0xFF
    if k==ord('q'):
        break

cv2.destroyAllWindows()
cam.release()
