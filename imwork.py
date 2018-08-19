import numpy as np
import cv2
#2D Convolution ( Image Filtering )

img=cv2.imread('olives.jpg',cv2.IMREAD_COLOR)

#kernel = np.ones((5,5),np.float32)/25 . The division is for averaging out all the pixels
kernel=np.ones((15,15),np.float32)/225
edged=np.array([[0,1,0],[1,-4,1],[0,1,0]])
edgee=np.array([[0,0,0],[-1,1,0],[0,0,0]])
blur=np.array([[1,1,1],[1,1,1],[1,1,1]])
sharp=np.array([[0,0,0,0,0],[0,0,-1,0,0],[0,-1,5,-1,0],[0,0,-1,0,0],[0,0,0,0,0]])
emboss=np.array([[-2,-1,0],[-1,1,1],[0,1,2]])

ie=cv2.filter2D(img,-1,edged)
iee=cv2.filter2D(img,-1,edgee)
ib=cv2.filter2D(img,-1,blur)
ih=cv2.filter2D(img,-1,sharp)
iem=cv2.filter2D(img,-1,emboss)
smooth=cv2.filter2D(img,-1,kernel)

#We should specify the width and height of kernel which should be positive and odd.
#We also should specify the standard deviation in X and Y direction, sigmaX and sigmaY respectively. If only sigmaX is specified, sigmaY is taken as same as sigmaX.
#If both are given as zeros, they are calculated from kernel size. Gaussian blurring is highly effective in removing gaussian noise from the image.
blurr=cv2.GaussianBlur(img,(15,15),0)

#Here, the function cv2.medianBlur() takes median of all the pixels under kernel area and central element is replaced with this median value.
#This is highly effective against salt-and-pepper noise in the images. Interesting thing is that, in the above filters, central element is a newly calculated value which may be a pixel value in the image or a new value.
#But in median blurring, central element is always replaced by some pixel value in the image.It reduces the noise effectively. Its kernel size should be a positive odd integer.
median=cv2.medianBlur(img,15)

#cv2.bilateralFilter() is highly effective in noise removal while keeping edges sharp. But the operation is slower compared to other filters. We already saw that gaussian filter takes the a neighbourhood around the pixel and find its gaussian weighted average.
# This gaussian filter is a function of space alone, that is, nearby pixels are considered while filtering. It doesn't consider whether pixels have almost same intensity.
# It doesn't consider whether pixel is an edge pixel or not. So it blurs the edges also, which we don't want to do.Bilateral filter also takes a gaussian filter in space, but one more gaussian filter which is a function of pixel difference.
#Gaussian function of space make sure only nearby pixels are considered for blurring while gaussian function of intensity difference make sure only those pixels with similar intensity to central pixel is considered for blurring. So it preserves the edges since pixels at edges will have large intensity variation.
bilateral=cv2.bilateralFilter(img,15,75,75)

cv2.imshow('Image-Edge',ie)
cv2.imshow('Image-Edge-Enhance',iee)
cv2.imshow('Image-Blur',ib)
cv2.imshow('Image-Sharp',ih)
cv2.imshow('Image-Emboss',iem)
cv2.imshow('MEDIAN',median)
cv2.imshow('BLUR',blurr)
cv2.imshow('bilateral',bilateral)
cv2.imshow('Image-Smooth',smooth)

cv2.waitKey(0)
cv2.destroyAllWindows()
