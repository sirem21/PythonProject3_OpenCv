import cv2 as cv
import numpy as np

img = cv.imread("1702829106037.jpg")
cv.imshow("orig", img)

grayscale = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

lap = cv.Laplacian(grayscale,cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow("laplacian", lap)

sobelX = cv.Sobel(grayscale,cv.CV_64F,1,0)
cv.imshow("sobelX", sobelX)

sobelY = cv.Sobel(grayscale,cv.CV_64F,0,1)
cv.imshow("sobelY", sobelY)

combined_sobel = cv.bitwise_or(sobelX,sobelY)
cv.imshow("sobel combined", combined_sobel)

cv.waitKey(0)
cv.destroyAllWindows()