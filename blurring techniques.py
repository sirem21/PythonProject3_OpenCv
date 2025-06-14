import cv2 as cv

img = cv.imread("1702829106037.jpg")
cv.imshow("Original",img)

# Averaging
average = cv.blur(img,(3,3))
#Median
median = cv.medianBlur(img,3)
# Gaussian
gaus = cv.GaussianBlur(img,(3,3),0)
# Bilateral
bilateral = cv.bilateralFilter(img,5,15,15)

cv.imshow("Average", average)
cv.imshow("Median", median)
cv.imshow("Gaussian", gaus)
cv.imshow("Bilateral",bilateral)
cv.waitKey(0)
cv.destroyAllWindows()