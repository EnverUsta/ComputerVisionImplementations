import  cv2
import numpy as np
from Resources import utlis


def nothing(_):
    pass


cap = cv2.VideoCapture('Resources/project_video.mp4')




#utlis.initializeTrackbars((10,10, 19, 19))

cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars", 360, 240)
cv2.createTrackbar('enver', "TrackBars", 11,  100, nothing)



arrayTest = np.zeros((5,5,5))
print(arrayTest)




while True:
    success, frame = cap.read()
    imgTest = frame[100:600, 100:500]
    imgTest2 = cv2.resize(frame, (300, 300))
    combinedImage, imgCanny, imgColor = utlis.thresholding(frame)
    cv2.imshow('output', imgTest)
    cv2.imshow('output2', imgTest2)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
