import cv2
import numpy as np
import matplotlib.pyplot as plt
tmg=cv2.imread('me.jpg')
cam=cv2.VideoCapture(0)
dst = cv2.resize(tmg, None, fx = 0.2, fy = 0.2, interpolation = cv2.INTER_CUBIC)
r,c,s=dst.shape

while True:
    ret,frame=cam.read()
    cv2.imshow('frame',frame)
    res=cv2.matchTemplate(frame,dst,cv2.TM_CCOEFF_NORMED)
    thresh=0.8
    loc=np.where(res>thresh)
    print(loc)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img , pt , (pt[0]+c , pt[1]+r) , (0,255,0) , 2)
    k=cv2.waitKey(1) & 0xFF
    if k==ord('q') or k==ord('Q'):
        break
cam.release()
cv2.destroyAllWindows()
