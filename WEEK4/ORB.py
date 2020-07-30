import cv2
import numpy as np

#ORB = FAST detector and BRIEF descriptor

img = cv2.imread('images/aeroplane.jpg')

ORB = cv2.ORB_create(50)
keyP, descriptor = ORB.detectAndCompute(img, None)

img2 = cv2.drawKeypoints(img, keyP, None, (255, 0, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow('Result', img2)
cv2.waitKey(0)
