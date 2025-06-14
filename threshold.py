import cv2 as cv

img = cv.imread("img1.jpg")
cv.imshow("orig", img)

threshold, thresh = cv.threshold(img, 150, 255, cv.THRESH_BINARY)