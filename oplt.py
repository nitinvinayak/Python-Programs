import cv2
import numpy
import matplotlib.pyplot as plt
img=cv2.imread('image.png',0) # 0 for grayscale
plt.imshow(img,cmap='gray',interpolation='bicubic')
plt.xticks([]),plt.yticks([])#Hides x,y coords
plt.show()
