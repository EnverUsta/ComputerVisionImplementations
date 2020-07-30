import cv2

cap = cv2.VideoCapture(0)

tracker = cv2.TrackerCSRT_create()
success, img = cap.read()
bbox = cv2.selectROI("Tracking", img, False)
tracker.init(img, bbox)

def drawTrackingBox(img, bbox):
    x,y,w,h = int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3])
    cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 255), 3, 3)
    cv2.putText(img, "Object Detected", (100, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,0, 0), 2)



while True:
    success, img = cap.read()
    success, bbox = tracker.update(img)

    if success:
        drawTrackingBox(img, bbox)
    else:
        cv2.putText(img, "Object Lost", (60, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,0,0), 2)

    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break