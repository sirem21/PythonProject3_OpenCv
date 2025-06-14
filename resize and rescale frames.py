import cv2 as cv
def resizing(img, scale):
    width = int(img.shape[1]*scale)
    height =int(img.shape[0]*scale)

    new_dimensions = (width,height)
    return cv.resize(img,new_dimensions,interpolation=cv.INTER_AREA)


# show image as pixel matrix
img = cv.imread("img1.jpg")
cv.imshow("or",img)

img_resized = resizing(img, 1.20)
cv.imshow("resized",img_resized)
cv.waitKey(0)
cv.destroyAllWindows()


