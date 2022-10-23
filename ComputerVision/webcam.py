import cv2

webcam = cv2.VideoCapture(0)

# we can also give address of video
#webcam = cv2.VideoCapture(r'C:\Users\mcups\Downloads')

while True: #or while webcam.isOpened():
    status,frame= webcam.read()    # status will store true or false
    if not status:
        print("Camera not working")
        break
    cv2.imshow("Webcam",frame)
    #press esc to exit
    if cv2.waitKey(10) == 27:
        break



webcam.release()
cv2.destroyAllWindows()