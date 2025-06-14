import cv2 as cv
import numpy as np

img =cv.imread('1702829106037.jpg')
cv.imshow("original",img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
blur = cv.blur(img,(5,5),cv.BORDER_DEFAULT)
canny = cv.Canny(img,125,175)

contour,hierarchy = cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
cv.drawContours(img, contour, -1, (0, 0, 255), 2)
cv.imshow('Contours', img)
print(f"{len(contour)} contours found!")
cv.imshow("canny",canny)

blank = np.zeros(img.shape,dtype='uint8')
cv.drawContours(blank, contour, -1, (0, 0, 255), 1)
cv.imshow('Contours on blank', blank)
print(f"{len(contour)} contours found!")
cv.imshow("canny",canny)

ret, thresh = cv.threshold(gray,125,255,cv.THRESH_BINARY)
cv.imshow("binary inv",thresh)

cv.waitKey(0)
cv.destroyAllWindows()