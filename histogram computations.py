import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("1702829106037.jpg")
grayscale = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# create a mask
mask = np.zeros(img.shape[:2], dtype='uint8')
mask[0:400, 100:200] = 255
#draw masked images
masked = cv.bitwise_and(grayscale,grayscale,mask = mask)
cv.imshow("Masked",masked)
masked2 = cv.bitwise_and(img,img, mask = mask)
cv.imshow("Masked Color",masked2)


# compare 2 histograms of a full image and of a masked image
hist = cv.calcHist([grayscale],[0],None,[256],[0,256])
hist_mask = cv.calcHist([grayscale],[0],mask,[256],[0,256])
plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("Number of pixels")
plt.plot(hist)
plt.plot(hist_mask)
plt.xlim([0,256])
plt.legend(["Hist","Hist_mask"])
plt.show()

# comparing the histograms
corr = cv.compareHist(hist, hist_mask, cv.HISTCMP_CORREL)
bhatt = cv.compareHist(hist, hist_mask, cv.HISTCMP_BHATTACHARYYA)
print(f"Correlation: {corr:.3f}  (1≈same)")
print(f"Bhattacharyya distance: {bhatt:.3f}  (0≈same)")

##########################
#Hist of colored image
colors = ('b','g','r')
#plt.figure("Full image histogram", figsize=(6,4))
for i,col in enumerate(colors):
    hist = cv.calcHist([img],[i],None,[256],[0,256])
    plt.plot(hist,color = col)
    plt.xlim([0,256])

plt.title("Colored Histogram")
plt.xlabel("Bins")
plt.ylabel("Number of pixels")
plt.show()

#plt.figure("Masked region histogram", figsize=(6,4))
for i,col in enumerate(colors):
    hist_mask = cv.calcHist([img], [i], mask, [256], [0, 256])
    plt.plot(hist_mask,color=col)
    plt.xlim([0,256])
plt.title("Colored Histogram Masked")
plt.xlabel("Bins")
plt.ylabel("Number of pixels")
plt.show()
cv.waitKey(0)
cv.destroyAllWindows()