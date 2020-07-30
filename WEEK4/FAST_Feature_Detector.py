import cv2

img = cv2.imread('images/aeroplane.jpg', 0)

detector = cv2.FastFeatureDetector_create(5)

kp = detector.detect(img, None)

img2 = cv2.drawKeypoints(img, kp, None, flags=0)




cv2.imshow('Corners', img2)
cv2.waitKey(0)

