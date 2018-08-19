import numpy as np
import cv2
import matplotlib.pyplot as plt

img=cv2.imread('clicked.jpg')
imgc=cv2.imread('click.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray=np.float32(gray)
grayc=cv2.cvtColor(imgc,cv2.COLOR_BGR2GRAY)
grayc=np.float32(grayc)
dst = cv2.cornerHarris(grayc,4,3,0.04)
dst = cv2.dilate(dst,None)
imgc[dst>0.01*dst.max()]=[0,0,255]
cv2.imshow('dst',imgc)

corners=cv2.goodFeaturesToTrack(gray,30,0.01,10)
corners=np.int0(corners)
for corner in corners:
        x,y=corner.ravel()
        cv2.circle(img,(x,y),4,255,-1)
cv2.imshow('IMG',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
