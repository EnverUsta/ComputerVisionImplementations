import matplotlib.pylab as plt
import cv2
import numpy as np

def region_of_interest(img, vertices):
    mask = np.zeros_like(img)
    #channel_count = img.shape[2]
    match_mask_color = 255
    cv2.fillPoly(mask, vertices, match_mask_color)
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image

def draw_the_lines(img, lines):
    img = np.copy(img)
    blank_image = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)
    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(blank_image, (x1, y1), (x2, y2), (255,255,0), thickness=4)

    img = cv2.addWeighted(img, 0.8, blank_image, beta=1, gamma=0.0)
    return img


#image = cv2.imread('Resources/road.jpg')
#image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

#print(image.shape)

def process(image):
    height = image.shape[0]
    width = image.shape[1]

    region_of_interest_vertices = [
        (0, height),
        (width/2, height/1.34),
        (width, height)
    ]

    grayImage = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    cannyImage = cv2.Canny(grayImage, 75, 250)
    cropped_image = region_of_interest(cannyImage,
                                   np.array([region_of_interest_vertices], np.int32),)

    lines = cv2.HoughLinesP(cropped_image,
                            rho=2,
                            theta=np.pi/60,
                            threshold=50,
                            lines=np.array([]),
                            minLineLength=50,
                            maxLineGap=100,
                            )
    image_with_lines = draw_the_lines(image, lines)
    return image_with_lines
    #plt.imshow(image_with_lines)
    #plt.show()

cap = cv2.VideoCapture("Resources/RoadTest.mp4")

while(cap.isOpened()):
    ret, frame = cap.read()
    frame = process(frame)
    cv2.imshow('Output', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()




