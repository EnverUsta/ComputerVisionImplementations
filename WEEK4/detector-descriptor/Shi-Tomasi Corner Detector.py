import cv2
import numpy as np

img = cv2.imread('images/aeroplane.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

corners = cv2.goodFeaturesToTrack(gray, 25, 0.01, 10)
corners = np.int0(corners)

for i in  corners:
        x, y = i.ravel()
        cv2.circle(img, (x, y), 2, (255, 0, 255), 2)

cv2.imshow('Shi-Thomas corner detection', img)
cv2.waitKey(0)

