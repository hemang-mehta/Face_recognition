#Generate the encodings of the faces as needed

import cv2
import face_recognition
import pickle
import os

#importing the student images
folderPath = "Images"
Pathlist = os.listdir(folderPath)
imgList = []
studentID = []
for path in Pathlist:
    imgList.append(cv2.imread(os.path.join(folderPath, path)))
    # print(path)
    # print(os.path.splitext(path)[0])
    studentID.append(os.path.splitext(path)[0])

print(studentID)

def findEncodings(imagesList):
    encodeList = []
    for img in imagesList:
        #Opencv uses BGR, face recognition uses RGB
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)

    return encodeList

encodeListKnown = findEncodings(imgList)
encodeListKnownwithids = [encodeListKnown, studentID]
print(encodeListKnown)

file = open("EncodeFile.p", "wb")
pickle.dump(encodeListKnownwithids, file)
file.close()
print("File saved")

