import os
import pickle
import cv2
import cvzone
import face_recognition
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
imgBackground = cv2.imread('Resources/bg.png')

# Importing the mode images into the list
folderModePath = 'Resources/Modes'
modePathList = os.listdir(folderModePath)
imgModeList = []
for path in modePathList:
    imgModeList.append(cv2.imread(os.path.join(folderModePath,path))) #imports images
print(len(imgModeList))

#load the encoding file
print("Loading encoding")
file = open('Encodefile.pkl','rb')
encodeListKnownWithIds = pickle.load(file) #loads everyhing from that file
file.close()
encodeListKnown, studentIds = encodeListKnownWithIds
print("Loading encoding.... Sucesss")
# print(studentIds)

while True:
    success, img = cap.read()
    imgS = cv2.resize(img,(0,0),None, 0.75,0.75)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    faceCurFrame = face_recognition.face_locations(imgS)
    encodeCurFrame = face_recognition.face_encodings(imgS,faceCurFrame)

    imgBackground[200:200 + 480,  55:55+640] = img
    imgBackground[44:44 + 148, 808:808+106] = imgModeList[0]

    for encodeFace, faceLocation in zip(encodeCurFrame,faceCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
        faceDistance = face_recognition.face_distance(encodeListKnown,encodeFace)
        print(faceDistance)
        print(matches)
        matchIndex = np.argmin(faceDistance)

        if matches[matchIndex]:
            # print("Known face detected")
            # print(studentIds[matchIndex])
            y1, x2, y2, x1 = faceLocation
            y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
            bbox= 55 + x1 ,  162+y1, x2-x1 , y2-y1
            imgBackground = cvzone.cornerRect(imgBackground,bbox,rt=0)

    cv2.imshow("Face Attendance", imgBackground)
    # cv2.imshow("Webcam", img)
    cv2.waitKey(1)
