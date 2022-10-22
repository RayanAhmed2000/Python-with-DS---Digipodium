import cv2

webcam = cv2.VideoCapture(0)

while True:
    status , frame = webcam.read()
    if not status:
        print("camera not working")
        break
    cv2.imshow("Webcam",frame)

    if cv2.waitkey(1) == 27:
        break
webcam.release()
cv2.destroyAllWindows()