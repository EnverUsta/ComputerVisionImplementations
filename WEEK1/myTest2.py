import cv2

cap = cv2.VideoCapture(0)
cap.set(3, 640)     #width
cap.set(4, 480)     #height
cap.set(10, 150)     #brightness


def faceDetection(img):
    faceCascade = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+h, y+h), (255, 0, 0), 2, cv2.LINE_4)
        addName(img, "enver", x, y)

def addName(img, name, x, y):
    cv2.putText(img, name, (x, y), cv2.FONT_ITALIC, 2, (0,0,0), 2)

def makeCannyEdgeDetection(img):
    imgCanny = cv2.Canny(img, 100, 100)
    cv2.imshow("Edge Detection", imgCanny)

while True:
    success, img = cap.read()
    imgCopy = img.copy()
    makeCannyEdgeDetection(imgCopy)
    faceDetection(img)
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



