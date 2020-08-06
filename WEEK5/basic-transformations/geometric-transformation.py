import cv2
import numpy as np

img = cv2.imread('images/red_panda.jpg')
rows, cols, ch = img.shape

scaled_img = cv2.resize(img, None, fx=1/2, fy=1/2)

matrix_translated = np.float32([[1,0,50], [0,1,50]])
translated_img = cv2.warpAffine(img, matrix_translated, (cols, rows))

#theta = 45
#matrix_rigid = np.float32([[np.cos(theta), -np.sin(theta), 0], [np.sin(theta), np.cos(theta), 0]])
matrix_r = cv2.getRotationMatrix2D((cols/2, rows/2), 90, 1)
rotated_img = cv2.warpAffine(img, matrix_r, (cols, rows))

cv2.imshow('original-image', img)
cv2.imshow('scaled-image', scaled_img)
cv2.imshow('translated-image', translated_img)
cv2.imshow('rigid-img', rotated_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
