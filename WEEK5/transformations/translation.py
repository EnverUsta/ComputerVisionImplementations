import argparse
import numpy as np
import cv2
import imutils

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())


image = cv2.imread(args["image"])
translation = imutils.translate(image, 100, 100)
cv2.imshow("Translation Down and Left", translation)

cv2.waitKey(0)

