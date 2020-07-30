import cv2
import numpy as np

img = cv2.imread("Resources/woman.jpg")
print(img.shape)

imgResize = cv2.resize(img, (300, 300))
print(imgResize.shape)

imgCropped = img[0:200, 200:500] #height, width

cv2.imshow("Woman", img)
cv2.imshow("Image resized", imgResize)
cv2.imshow("Image cropped", imgCropped)
cv2.waitKey(0)