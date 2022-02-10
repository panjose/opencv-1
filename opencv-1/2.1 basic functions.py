# -*-coding:utf-8 -*-
# Date:2022.01
# Creator:Panjose
# Product:2.1 basic functions.py
import cv2
import numpy as np

img = cv2.imread("resources/lena.png")
kernel = np.ones((5, 5), np.uint8)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 变灰色
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)
# 模糊：（'7,7'：必须是奇数，两个值要相同）
imgCanny = cv2.Canny(img, 100, 100)
# 扣轮廓：（数值越大轮廓越少）
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)
# 膨胀
imgEroded = cv2.erode(imgDialation,kernel,iterations=1)
# 腐蚀

cv2.imshow("Grey Image", imgGray)
cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dialation Image", imgDialation)
cv2.imshow("Eroded Image", imgEroded)
cv2.waitKey(0)
