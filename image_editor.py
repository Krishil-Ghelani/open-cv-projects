#importing packages
import cv2
import numpy as np
img = cv2.imread("C:/Users/Ashish/PycharmProjects/openCV/resources/meme.jpeg")
# print(img)
kernel = np.ones((5,5), np.uint8)
cv2.imshow("nothing", img)
imgraph = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imblur = cv2.GaussianBlur(imgGray, (17, 17), 0)
imgCanny = cv2.Canny(img, 100, 100)
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)
imgeroded = cv2.erode(imgDialation, kernel, iterations=1)

cv2.imshow("Gray image", imgraph)
cv2.imshow("blur image", imblur)
cv2.imshow("canny image", imgCanny)
cv2.imshow("dialation image", imgDialation)
cv2.imshow("eroded image", imgeroded)




cv2.waitKey(0)