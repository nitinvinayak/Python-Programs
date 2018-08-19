import numpy as np
import cv2

img=cv2.imread('tempsearch.jpg')
template=cv2.imread('temptemp.jpg')

r,c,s=template.shape

res=cv2.matchTemplate(img,template,cv2.TM_CCOEFF_NORMED)
thresh=0.5
count=0
loc=np.where(res>thresh)

for pt in zip(*loc[::-1]):
    cv2.rectangle(img , pt , (pt[0]+c , pt[1]+r) , (0,255,0) , 2)
    count+=1
    #print(img[list(pt)])
    #cv2.imshow('img'+str(count),img[list(pt)])
cv2.imshow('det',img)
cv2.imshow('TEMP',template)
print(count)
cv2.waitKey(0)
cv2.destroyAllWindows()
              
