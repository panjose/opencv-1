# -*-coding:utf-8 -*-
# Date:2022.01
# Creator:Panjose
# Product:1.1 photo.py
import cv2

img = cv2.imread("resources/lena.png")
cv2.imshow("Output", img)
cv2.waitKey(0)
