import cv2
import os

cap = cv2.VideoCapture(0)
cap.set(3,640) #set width
cap.set(4,480) #set height


imgBackground = cv2.imread('Resources/background.png')


#importing the mode images into a list
folderModePath = "Resources/Modes"
modePath = os.listdir(folderModePath)
imgModeList = []

for path in modePath:
    imgModeList.append(cv2.imread(os.path.join(folderModePath, path)))



#displaying the finnal product
while True:
    success, img = cap.read()
    imgBackground[162:642, 55:695] = img 
    imgBackground[44:677, 808:1222] = imgModeList[3]
    cv2.imshow("Face Attendance", imgBackground)
    if cv2.waitKey(1) & 0xFF==ord('r'):
        break

cap.release()
cv2.destroyAllWindows()