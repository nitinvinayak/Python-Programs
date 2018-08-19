import cv2
import numpy
import matplotlib.pyplot as plt
#path = 'photos'
c1=cv2.VideoCapture(0)
#c2=cv2.VideoCapture(1)
while True:
    ret1,frame1=c1.read()
    #ret2,frame2=c2.read()
    cv2.imshow('webcam-of-laptop',frame1)
    #cv2.imshow('webcam-microsoft',frame2)
    if cv2.waitKey(1)==ord('q'):
        break
    elif cv2.waitKey(1)==ord('c'):
        cv2.imwrite('image1.jpg',frame1)
        #cv2.imwrite('image2.jpg',frame2)
c1.release()
#c2.release()
cv2.destroyAllWindows()
