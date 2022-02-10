# -*-coding:utf-8 -*-
# Date:2022.01
# Creator:Panjose
# Product:1.2 video.py
import cv2

cap = cv2.VideoCapture("resources/test_video.mp4")

while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
