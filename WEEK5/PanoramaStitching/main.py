import cv2
import os

mainFolder = 'Images'
myFolders = os.listdir(mainFolder)




for folder in myFolders:
    path = mainFolder + '/' + folder
    images = []
    myList = os.listdir(path)
    print(f'Total Number of images detected {len(myList)}')
    for nImg in myList:
        curImg = cv2.imread(f'{path}/{nImg}')
        curImg = cv2.resize(curImg, (0, 0), dst=None, fx=0.2, fy=0.2)
        images.append(curImg)

    stitcher = cv2.Stitcher_create()
    (status, result) = stitcher.stitch(images=images)
    if(status == cv2.Stitcher_OK):
        print('Panaroma Generated')
        cv2.imshow(folder, result)
    else:
        print('Panaroma Generation Unsuccessful')





cv2.waitKey(0)
