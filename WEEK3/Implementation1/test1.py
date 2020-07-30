import cv2
import numpy as np

img = cv2.imread('Resources/road.jpg')


arrayExample = np.zeros((5, 5))
arrayExample2 = np.zeros_like(img)
arrayExample3 = np.array([1, 4, 4, 5])
arrayExample4 = np.array([1, 3, 4, 5])
masked = np.bitwise_or(arrayExample3, arrayExample4)
print(masked)
#print(arrayExample3)
#print(arrayExample)



