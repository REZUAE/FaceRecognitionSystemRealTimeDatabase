import os

import cv2

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(3, 480)
imgBackground = cv2.imread('Resources/bg.png')

# Importing the mode images into the list
folderModePath = 'Resources/Modes'
modePathList = os.listdir(folderModePath)
imgModeList = []
for path in modePathList:
    imgModeList.append(cv2.imread(os.path.join(folderModePath,path))) #imports images
print(len(imgModeList))

while True:
    success, img = cap.read()
    imgBackground[200:200 + 480,  55:55+640] = img
    imgBackground[44:44 + 148, 808:808+106] = imgModeList[0]

    cv2.imshow("Face Attendance", imgBackground)
    # cv2.imshow("Webcam", img)
    cv2.waitKey(1)
