import cv2
import numpy as np

#Detector parameters
block_size = 2
k_size = 7
k = 0.04


img = cv2.imread('images/grains.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

harris = cv2.cornerHarris(gray, block_size, k_size, k)

img[harris > 0.01 * harris.max()] = [255, 0, 0]

cv2.imshow('Harris', img)
cv2.waitKey(0)
