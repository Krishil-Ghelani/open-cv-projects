import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)


mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
Face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_defult.xml')
upper_body = cv2.CascadeClassifier('upperbody.xml')




while True:
    success, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = Face_cascade.detectMultiScale(gray, 1.1, 4)
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    result = hands.process(imgRGB)
    UPPER_BODY = upper_body.detectMultiScale(gray, 1.1, 4)
    UBRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    # print(result.multi_hand_landmarks)
    if result.multi_hand_landmarks:
        for handLms in result.multi_hand_landmarks:
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cv2.imshow("Image",img)
    cv2.imshow('imageUpperBody', UBRGB)
    cv2.waitKey(1)