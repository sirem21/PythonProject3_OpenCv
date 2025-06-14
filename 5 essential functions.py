import cv2 as cv

img = cv.imread("img1.jpg")
cv.imshow("orig", img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gray image", gray)

blur = cv.GaussianBlur(img,(71,71),cv.BORDER_DEFAULT)
cv.imshow("blur",blur)

canny = cv.Canny(blur,255,0)
cv.imshow("edges", canny)

cropped = img[0:10, 10:500]
cv.imshow("cropped", cropped)
cv.waitKey(0)
cv.destroyAllWindows()


