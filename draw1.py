import numpy as np
import cv2
img=cv2.imread('image.png',cv2.IMREAD_COLOR)
cv2.line(img , (0,0) , (250,250) , (255,255,255) , 10 ) #bgr not rgb
cv2.rectangle(img, (15,20),(100,200),(230,32,23),15) #top-left coords, bottom-right coords
#cv.LINE_AA for curves(also for text), in place of line type
cv2.circle(img,(300,120),100,(0,0,255), 23)# Centre,radius and if line width is negative it fills the circle
#putText(img, text, org, fontFace, fontScale, color[,thickness[, lineType[, bottomLeftOrigin]]]) -> img
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'HEY!',(375,200),font,3,(200,220,0),3)
#polylines(img, pts, isClosed, color[, thickness[, lineType[, shift]]]) -> img
pts=np.array([[120,20],[200,25],[75,30]],np.int32)
cv2.polylines(img,[pts],True,(0,20,245),1)
cv2.imshow('im',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
