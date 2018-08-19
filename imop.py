import cv2
import numpy as np
img=cv2.imread('image.png',cv2.IMREAD_COLOR)
#Image operations
px=img[30,40] #Shows the pixel colour for that location
print(px)
part=img[200:230,220:300]#copy
img[0:30,0:80]=part#paste
#img[100:130,100:130]=[23,45,67] #Using the ROI-region of image
cv2.imshow('img',img)
cv2.waitKey(0)# 0 corresponds to forever
cv2.destroyAllWindows()
