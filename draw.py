import numpy as np
import cv2 as cv

blank = np.zeros((500,500,3), dtype='uint8')
blank[200:300, 300:400] = 0,0,255

cv.putText(blank,"Hello",(220,220),cv.FONT_HERSHEY_TRIPLEX,3.0,(0,255,0),thickness=2)
cv.imshow("blank", blank)
cv.waitKey(0)
cv.destroyAllWindows()