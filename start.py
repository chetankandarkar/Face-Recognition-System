import cv2
video_capture = cv2.VideoCapture(0)

while True:
    _,img = video_capture.read()
    cv2.imshow("Heading of the screen shown",img)
    if cv2.waitKey(1)&0xFF == ord('q'):
        break
video_capture.realease()
cv2.destroyWindow()