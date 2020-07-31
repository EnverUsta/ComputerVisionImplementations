import cv2
import numpy as np


def feature_match(img1, img2):
    orb = cv2.ORB_create()
    kp1, des1 = orb.detectAndCompute(img1, None)
    kp2, des2 = orb.detectAndCompute(img2, None)
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(des1, des2)
    matches = sorted(matches, key=lambda x:x.distance)
    matching_result = cv2.drawMatches(img1, kp1, img2, kp2, matches[:10], None, flags=2)
    return matching_result



cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
cap.set(10, 150)

while True:
    success, capImage = cap.read()
    imgBook = cv2.imread('images/book.png')
    matching_result = feature_match(imgBook, capImage)
    cv2.imshow('Matching Result', matching_result)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

