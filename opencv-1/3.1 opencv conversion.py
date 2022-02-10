# -*-coding:utf-8 -*-
# Date:2022.01
# Creator:Panjose
# Product:3.1 opencv conversion.py
import cv2
import numpy as np

img = cv2.imread("resources/lambo.PNG")
print(img.shape)

imgResize = cv2.resize(img, (300, 200))
print(imgResize.shape)

imgCropped = img[0:200, 200:500]

cv2.imshow("Image", img)
cv2.imshow("Image Resize", imgResize)
cv2.imshow("Image Cropped", imgCropped)

cv2.waitKey(0)
