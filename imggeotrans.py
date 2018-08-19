import cv2
import numpy as np
import matplotlib.pyplot as plt
#Scaling Images
# cv2.INTER_LINEAR for all resizing purposes-INTERPOLATION
img=cv2.imread('olives.jpg',cv2.IMREAD_COLOR)

res=cv2.resize(img,None,fx=2,fy=2,interpolation=cv2.INTER_CUBIC)
#OR
h,w,c=img.shape
rest=cv2.resize(img,(2*w,2*h),interpolation=cv2.INTER_CUBIC)
#cv2.imshow('res',res)
#cv2.imshow('rest',rest)

#Translation
#M is the transition matrix
rows,cols,chan = img.shape
#for a shift of (100,50), generally array format is [1,0,x,],[0,1,y]
M = np.float32([[1,0,100],[0,1,50]])
dst = cv2.warpAffine(img,M,(cols,rows))
cv2.imshow('dst',dst)

#Rotation
#the arguments are rotation center, angle, and magnification
M1 = cv2.getRotationMatrix2D((cols/2,rows/2),45,1)
dstt=cv2.warpAffine(img,M1,(cols,rows))
cv2.imshow('dstt',dstt)

#Affline Transformation

pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])
     
M2 = cv2.getAffineTransform(pts1,pts2)
dsr = cv2.warpAffine(img,M,(cols,rows))
    
plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dsr),plt.title('Output')
#plt.show()

#Perspective Transformation
pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])
     
M = cv2.getPerspectiveTransform(pts1,pts2)

dst = cv2.warpPerspective(img,M,(300,300))
#plt.subplot(nrows, ncols, index, **kwargs)
plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()

