import numpy as np 
import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

#cap = cv2.VideoCapture(0)

#while(True):
#ret, frame = cap.read()

frame = cv2.imread('baby.png')

#gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#gray = cv2.equalizeHist(gray)

#Detect faces
# faces = face_cascade.detectMultiScale(gray, 1.3, 5)
# print len(faces)
# #print(faces.length)
# for (x,y,w,h) in faces:
# 	cv2.rectangle(gray, (x,y), (x+w,y+h), (255,0,0), 2)

# faces = face_cascade.detectMultiScale(gray, 1.3, 5)
# for (x,y,w,h) in faces:
#     cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
#     roi_gray = gray[y:y+h, x:x+w]
#     roi_color = img[y:y+h, x:x+w]
#     eyes = eye_cascade.detectMultiScale(roi_gray)
#     for (ex,ey,ew,eh) in eyes:
#         cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)


#frame = cv2.Canny(frame,100,200)

cv2.imshow('frame', frame)
cv2.waitKey(0)

#cap.release()
cv2.destroyAllWindows()
