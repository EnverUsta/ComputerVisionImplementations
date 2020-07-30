import cv2

cap = cv2.VideoCapture(0)
cap.set(3, 640)     #width
cap.set(4, 480)     #height
cap.set(10, 150)    #brightness


def detectCorners(img):
    detector = cv2.FastFeatureDetector_create(50, nonmaxSuppression=True)
    keyPoints = detector.detect(img, None)
    img2 = cv2.drawKeypoints(img, keyPoints, None, color=(255, 0, 255))
    return img2





while True:
    success, img = cap.read()
    result = detectCorners(img)
    cv2.imshow("Video", result)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
