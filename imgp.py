import numpy as np
import cv2
from matplotlib import pyplot as plt

#path = '/Users/RohanSaxena/Documents/projects/cv'
image = cv2.imread('olives.jpg')

np.shape(image)

# Select the individual channels:
blue = image[:, :, 0]
green = image[:, :, 1]
red = image[:, :, 2]

plt.imshow(blue, cmap='Blues')
plt.show()

plt.imshow(green, cmap='Greens')
plt.show()

plt.imshow(red, cmap='Reds')
plt.show()

''' We need to do the following because openCV reads in an RGB image's pixel
values as BGR values. So the individual channels have to be stacked over each
other over the last axis '''
image = np.stack([image[:, :, 2], image[:, :, 1], image[:, :, 0]], axis=-1)

plt.imshow(image)
plt.show()
