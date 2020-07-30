import cv2
import numpy as np

img1 = cv2.imread('images/book.png', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('images/holding_book.jpeg', cv2.IMREAD_GRAYSCALE)

#ORB detector
orb = cv2.ORB_create()
kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

#Brute force matching
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

#Match descriptors
matches = bf.match(des1, des2)

#Sort them in the order of their distance
matches = sorted(matches, key=lambda x:x.distance)

#Draw first 10 matches
matching_result = cv2.drawMatches(img1, kp1, img2, kp2, matches, None)



cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('result', matching_result)

cv2.waitKey(0)
cv2.destroyAllWindows()



