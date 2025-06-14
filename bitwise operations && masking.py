import cv2 as cv
import numpy as np

# draw 2 images of square and a circle
blank = np.zeros((400,400),dtype='uint8')
rectangle = cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)
circle = cv.circle(blank.copy(),(200,200),180,255,-1)
cv.imshow("Rectagle",rectangle)
cv.imshow("Circle", circle)

# bitwise AND
img_and = cv.bitwise_and(rectangle,circle)
cv.imshow("AND", img_and)

# bitwise OR
img_or = cv.bitwise_or( rectangle,circle)
cv.imshow("OR", img_or)

# bitwise XOR
img_xor = cv.bitwise_xor(rectangle,circle)
cv.imshow("XOR", img_xor)

# bitwise NOT
img_not = cv.bitwise_not(circle)
cv.imshow("NOT", img_not)

#MASK
img =cv.imread('1702829106037.jpg')
def masked(img):
    blank = np.zeros(img.shape[:2],dtype='uint8')
    circle = cv.circle(blank,(img.shape[1]//2+80,img.shape[0]//2-100), 100, 255,-1)
    masked_img = cv.bitwise_and(img,img,mask=circle)
    return masked_img
cv.imshow("Masked",masked(img))

cv.waitKey(0)
cv.destroyAllWindows()