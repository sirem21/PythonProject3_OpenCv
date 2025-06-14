import cv2 as cv

# show image as pixel matrix
img = cv.imread("img1.jpg")
# show image in new window
cv.imshow("or",img)

# show the window for ... miliseconds
# if is 0 --> it can wait independently unlit we will press the button
cv.waitKey(0)

# It ensures that all the image display windows (created with cv.imshow) are properly closed.
# Without this, the windows might stay open even after your program finishes,leading to frozen or unresponsive windows.
cv.destroyAllWindows()

#open VIDEO
# as arguments can be NUMBERS(if you get video from your camera, by default 0 for your computer's camera and else for different ones)
# or 'name of existing videos'
capture = cv.VideoCapture('dog.mp4')

#Read the VIDEO
# for reading the video we need loop because we will read the video frame(kadr) by frame
while True:
    isTrue, frame = capture.read()
    cv.imshow('dog.mp4',frame)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break
capture.release()
cv.destroyAllWindows()