import cv2
import numpy as np


img = np.zeros((512, 512, 3), np.uint8)
cv2.line(img, (0,0), (100, 100), (0,255,0), 1)

cv2.imshow("Output", img)
cv2.waitKey(0)
