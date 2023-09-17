import cv2
import face_recognition
import pickle
import os
import firebase_admin
from firebase_admin import credentials, db , storage

cred = credentials.Certificate("ficeattendancerealtime-firebase-adminsdk-t4txi-676cfc11fc.json") #ENTER YOUR OWN DATABASE KEY
firebase_admin.initialize_app(cred,{
    'databaseURL': "https://ficeattendancerealtime-default-rtdb.firebaseio.com/",
    'storageBucket': "ficeattendancerealtime.appspot.com"
})
# Importing the students
folderPath = 'Images'
PathList = os.listdir(folderPath)
imgList = []
studentIds = []
for path in PathList:
    imgList.append(cv2.imread(os.path.join(folderPath,path))) #imports images
    studentIds.append(os.path.splitext(path)[0])#gets the ID from path image name

    fileName = f'{folderPath}/{path}'
    bucket = storage.bucket()
    blob = bucket.blob(fileName)
    blob.upload_from_filename(fileName)

print(len(imgList))
print(studentIds)

def findEncodings(imagesList):
    encodeList = []
    for img in imagesList:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)

        return encodeList

print('encoding started')
encodeListKnown = findEncodings(imgList)
encodeListKnownWithIds = [encodeListKnown,studentIds]
print('encoding complete')

file = open('Encodefile.pkl', 'wb') #opens a file and puts 2 lists
pickle.dump(encodeListKnownWithIds, file)
file.close()
print("File saved")
