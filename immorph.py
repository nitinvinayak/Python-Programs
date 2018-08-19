import cv2
import numpy as np

cam=cv2.VideoCapture(0)

while True:
    ret,frame=cam.read()
    #hue,saturation, value
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lower=np.array([170,50,0])
    upper=np.array([179,255,255])

    mask=cv2.inRange(hsv,lower,upper)
    res=cv2.bitwise_and(frame,frame,mask=mask)

    kernel=np.ones((5,5),np.uint8)

    mask=cv2.filter2D(mask,-1,kernel)
    # it erodes away the boundaries of foreground object.The kernel slides through the image (as in 2D convolution). A pixel in the original image (either 1 or 0) will be considered 1 only if all the pixels under the kernel is 1, otherwise it is eroded (made to zero).
    #So what happends is that, all the pixels near boundary will be discarded depending upon the size of kernel. So the thickness or size of the foreground object decreases or simply white region decreases in the image.
    #It is useful for removing small white noises (as we have seen in colorspace chapter), detach two connected objects etc.
    erosion=cv2.erode(mask, kernel, iterations=1)

    #It is just opposite of erosion. Here, a pixel element is '1' if atleast one pixel under the kernel is '1'. So it increases the white region in the image or size of foreground object increases. Normally, in cases like noise removal, erosion is followed by dilation. 
    # Because, erosion removes white noises, but it also shrinks our object. So we dilate it. Since noise is gone, they won't come back, but our object area increases. It is also useful in joining broken parts of an object.
    dilation=cv2.dilate(mask, kernel, iterations=1)

    #Opening is just another name of erosion followed by dilation. It is useful in removing noise, as we explained above.
    opening=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)

    #Closing is reverse of Opening, Dilation followed by Erosion. It is useful in closing small holes inside the foreground objects, or small black points on the object.
    closing=cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel)

    #Morphological Gradient
    #It is the difference between dilation and erosion of an image.
    gradient = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernel)#Comes like an edge with like noise

    #Top Hat
    #It is the difference between input image and Opening of the image.
    tophat = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernel)

    #Black Hat
    #It is the difference between the closing of the input image and input image.
    blackhat = cv2.morphologyEx(mask, cv2.MORPH_BLACKHAT, kernel)
    
    cv2.imshow('frame',frame)
    cv2.imshow('res',res)
    cv2.imshow('CLOSING',closing)
    cv2.imshow('OPENING',opening)
    cv2.imshow('dilation',dilation)
    cv2.imshow('erosion',erosion)
    cv2.imshow('GRADIENT',gradient)
    cv2.imshow('TOP HAT',tophat)
    cv2.imshow('BLACK HAT',blackhat)
    
    k=cv2.waitKey(1) & 0xFF
    if k==ord('q') or k==ord('Q'):
        break

cv2.destroyAllWindows()
cam.release()
