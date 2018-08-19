import cv2
import numpy as np
img1=cv2.imread('image1.jpg',cv2.IMREAD_COLOR)
#img2=cv2.imread('image2.jpg',cv2.IMREAD_COLOR)
img3=cv2.imread('olives.jpg',cv2.IMREAD_COLOR)

rows,cols,channels=img3.shape

roi=img1[0:rows,0:cols]

img32gray=cv2.cvtColor(img3,cv2.COLOR_BGR2GRAY) #GRAYED OUT IMAGE

ret,mask=cv2.threshold(img32gray,100,255,cv2.THRESH_BINARY)#cv2.THRESH_BINARY_INV

mask_inv=cv2.bitwise_not(mask)

img1_bg=cv2.bitwise_and(roi,roi,mask=mask_inv)
img2_fg=cv2.bitwise_and(img3,img3,mask=mask)

dst=cv2.add(img1_bg,img2_fg)
img1[0:rows,0:cols]=dst 

cv2.imshow('result',img1)
cv2.imshow('bg',img1_bg)
cv2.imshow('fg',img2_fg)
cv2.imshow('mask',mask)
cv2.imshow('dst',dst)
cv2.imshow('maskinv',mask_inv)
#add=img1+img2
#add=cv2.add(img1,img2)
#weighted=cv2.addWeighted(img1,0.5,img2,0.5,0)
#cv2.imshow('weighted',weighted)
cv2.waitKey(0)
cv2.destroyAllWindows()
