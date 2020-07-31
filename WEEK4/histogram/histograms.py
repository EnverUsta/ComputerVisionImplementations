import cv2
import numpy as np
from matplotlib import pyplot as plt

img = np.zeros((100, 100), np.uint8)
cv2.rectangle(img, (25, 25), (75, 75), (255), -1)

cv2.imshow('img', img)
cv2.waitKey(0)

plt.hist(img.ravel(), 256, [0, 256])
plt.show()
