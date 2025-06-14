import cv2 as cv

img = cv.imread("1702829106037.jpg")
cv.imshow("orig", img)

grayscale = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# Simple Threshold
threshold, thresh = cv.threshold(grayscale, 150, 255, cv.THRESH_BINARY)
cv.imshow("simple", thresh)
# Adaptive Threshold
adapt_threshold = cv.adaptiveThreshold(grayscale,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,1 )
cv.imshow("Adaptive", adapt_threshold)

cv.waitKey(0)
cv.destroyAllWindows()