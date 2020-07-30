import cv2
import numpy as np


cap = cv2.VideoCapture(0)
cap.set(3, 640)     #width
cap.set(4, 480)     #height
cap.set(10, 150)     #brightness


myColours = [[155, 84, 0, 179, 232, 255], [63,0,108,87,40,166]]  #h_min, s_min, v_min; h_max, s_max, v_max
namesOfObjects = ["Rubber", "Thermos"]

def findColour(img):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count = 0
    for color in myColours:
        lowerB = np.array([color[0:3]])
        upperB = np.array([color[3:6]])
        mask = cv2.inRange(imgHSV, lowerB, upperB)
        x, y, w, h = getContours(mask)
        #cv2.circle(mask, (x,y), 10, (255, 0, 0), 3)
        cv2.rectangle(resultImage, (x,y), (x+w, y+h), (255, 0, 0), 2)
        cv2.putText(resultImage, namesOfObjects[count], (x, y), cv2.FONT_ITALIC, 1, (0,0,0), 2)
        count += 1
        #cv2.imshow("mask", mask)



def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x, y, w, h = 0, 0, 0, 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 400:
            cv2.drawContours(img, cnt, -1, (0, 0, 0))
            arcLength = cv2.arcLength(cnt, True)
            #cornerArray = cv2.approxPolyDP(img, 0.02*arcLength, True)
            #numberOfCorners = len(cornerArray)
            x, y, w, h = cv2.boundingRect(cnt)
    return x, y, w, h




while True:
    success, img = cap.read()
    resultImage = img.copy()
    testCannyImage = cv2.Canny(img, 100, 100)
    findColour(img)
    cv2.imshow("Video", img)
    cv2.imshow("Result", resultImage)
    cv2.imshow("CannyImage", testCannyImage)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break