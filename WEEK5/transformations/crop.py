import cv2
import argparse


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

cropped = image[:240 , 120:360]
cv2.imshow("Cropped", cropped)

cv2.waitKey(0)
