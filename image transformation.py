import cv2 as cv
import numpy as np
from numpy.f2py.crackfortran import dimensionpattern

img = cv.imread("img1.jpg")
cv.imshow("or",img)

def translate(img,x,y):
    new_image = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[0],img.shape[1])
    return cv.warpAffine(img,new_image,dimensions)

# -x --> Left
#  x --> Right
# -y --> Up
#  y --> Down

translated = translate(img,-100,200)
cv.imshow("Translated", translated)

# Rotation
def rotate(img, rotation_angle, rotPoint = None):
    if rotPoint is None:
        rotPoint = (int(img.shape[1] //2), int(img.shape[0] // 2))
    rotMat = cv.getRotationMatrix2D(rotPoint,rotation_angle,1.0)
    dimension = (img.shape[0], img.shape[1])
    return cv.warpAffine(img, rotMat, dimension)
rotated = rotate(img, -90)
cv.imshow("Rotated", rotated)


#Flipping
flipped = cv.flip(img,-1)
cv.imshow("Flipped", flipped)
cv.waitKey(0)
cv.destroyAllWindows()
