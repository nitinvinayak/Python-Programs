import numpy as np
import cv2

img=cv2.imread('clicked.jpg')
template=cv2.imread('click.jpg')

r,c,s=template.shape

res=cv2.matchTemplate(img,template,cv2.TM_CCOEFF_NORMED)
thresh=0.99
count=0
loc=np.where(res>thresh)

for pt in zip(*loc[::-1]):
    cv2.rectangle(img , pt , (pt[0]+c , pt[1]+r) , (0,255,0) , 2)
    count+=1
    #print(img[list(pt)])
    print(pt[0],pt[1],pt[0]+c , pt[1]+r)
    #cv2.imshow('img'+str(count),img[list(pt)])
print(count)
cv2.imshow('det',img)
cv2.imshow('res',res)
cv2.waitKey(0)
cv2.destroyAllWindows()
              
