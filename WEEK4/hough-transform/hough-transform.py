import cv2
import numpy as np

img = cv2.imread('images/line.png', cv2.IMREAD_GRAYSCALE)
img = cv2.GaussianBlur(img, (5,5), 10)
edges = cv2.Canny(img, 50, 150, apertureSize=3)

lines = cv2.HoughLines(edges, 1, np.pi/180, 200)

for rho, theta in lines[0]:
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho
    x1 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * (a))
    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * (a))


cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)

cv2.imshow('ResultImage', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

