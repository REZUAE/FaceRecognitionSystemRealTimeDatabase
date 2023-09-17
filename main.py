import cv2

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(3, 720)

while True:
    success, img = cap.read()
    cv2.imshow("Face Attednance", img)
    cv2.waitKey(1)