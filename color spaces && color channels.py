import cv2 as cv
import numpy as np


img = cv.imread("1702829106037.jpg")
"""
grayscale = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("BGR --> Grayscale", grayscale)

hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow("BGR --> HSV", hsv)

lab = cv.cvtColor(img,cv.COLOR_BGR2Lab)
cv.imshow("BGR --> LAB", lab)

rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow("BGR --> RGB", rgb)

g_to_bgr = cv.cvtColor(cv.cvtColor(grayscale,cv.COLOR_GRAY2BGR),cv.COLOR_BGR2HSV)
cv.imshow("Grayscale --> HSV", g_to_bgr)

cv.waitKey(0)
cv.destroyAllWindows()
"""


######## COLOR CHANNELS ###########

b,g,r = cv.split(img)
cv.imshow("blue",b)
cv.imshow ("red", r)
cv.imshow("green", g)


blank = np.zeros(img.shape[:2], dtype = 'uint8')
img_new = cv.merge([b,g,r],blank)

blue = cv.merge([b,blank,blank])
cv.imshow(" full blue", blue)

red = cv.merge([blank,blank,r])
cv.imshow("full red", red)

green = cv.merge([blank,g,blank])
cv.imshow("full green", green)

cv.imshow("Merged Channels",img_new)
cv.waitKey(0)
cv.destroyAllWindows()