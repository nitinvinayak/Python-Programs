import numpy as np
import cv2
import matplotlib.pyplot as plt

imgr = cv2.imread('clicked.jpg')
#cv2.imshow('img',imgr)
r,c,s=imgr.shape
mask = np.zeros(imgr.shape[:2],np.uint8)

bgdModel=np.zeros((1,65),np.float64)
fgdModel=np.zeros((1,65),np.float64)

rect=(195,25,500,346)

cv2.grabCut(imgr,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)

mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')

imgf=imgr*mask2[:,:,np.newaxis]
plt.imshow(imgf)
plt.colorbar()
plt.show()
