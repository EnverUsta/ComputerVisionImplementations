import cv2
import numpy as np

img = cv2.imread("Resources/cards.jpg")

width, height = 300, 450
pts1 = np.float32([[338,32], [502,139], [180, 266], [351, 377]])
pts2 = np.float32([[0,0], [width, 0], [0, height], [width, height]])

matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOutput = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow("Image",img)

cv2.imshow("OutputImage", imgOutput)
cv2.imwrite("Resources/card10.jpg", imgOutput)


cv2.waitKey(0)