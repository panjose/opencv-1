# -*-coding:utf-8 -*-
# Date:2022.01
# Creator:Panjose
# Product:1.3 camera.py
import cv2

cap = cv2.VideoCapture(0)
cap.set(3, 640)  # 宽度
cap.set(4, 480)  # 高度
cap.set(10, 100)  # 亮度

while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
