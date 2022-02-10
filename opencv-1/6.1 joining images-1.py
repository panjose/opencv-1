# -*-coding:utf-8 -*-
# Date:2022.01
# Creator:Panjose
# Product:6.1 joining images-1.py
import cv2
import numpy as np

img = cv2.imread("resources/lena.png")
imgHor = np.hstack((img, img))
imgVer = np.vstack((img, img))

cv2.imshow("Horizontal", imgHor)
cv2.imshow("Vertical", imgVer)

cv2.waitKey(0)
