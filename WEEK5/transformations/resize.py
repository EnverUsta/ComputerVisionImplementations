import argparse
import numpy as np
import cv2
import imutils

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())


image = cv2.imread(args["image"])
cv2.imshow("Original", image)

resized = imutils.resize(image, height=200, width=None, inter=None)
cv2.imshow("Resized", resized)


cv2.waitKey(0)
