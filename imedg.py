import cv2
import numpy as np

cam=cv2.VideoCapture(0)

while True:
    ret,frame=cam.read()

    sobelx=cv2.Sobel(frame,cv2.CV_64F,1,0,ksize=5)
    sobely=cv2.Sobel(frame,cv2.CV_64F,0,1,ksize=5)
    #Edge detector the dimension is for the size of the kernel
    edge=cv2.Canny(frame,50,100)
    
    laplace=cv2.Laplacian(frame,cv2.CV_64F)
    
    #cv2.imshow('sobelx',sobelx)
    #cv2.imshow('sobely',sobely)
    #cv2.imshow('laplace',laplace)
    cv2.imshow('edge',edge)
    
    k=cv2.waitKey(1) & 0xFF
    if k==ord('q'):
        break

cv2.destroyAllWindows()
cam.release()

