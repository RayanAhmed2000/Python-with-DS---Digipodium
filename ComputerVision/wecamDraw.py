from datetime import datetime
import cv2

webcam = cv2.VideoCapture(0)

while True: 
    status, img= webcam.read()   
    if not status:
        print("Camera not working")
        break
    
    #CHANGING THE SIZE OF FRAME WINDOW
    '''h,w,_=img.shape
    img = cv2.resize(img,(w*2,h*2))
    '''
    #DISPLAYING DATE AND TIME ON SCREEN
    def get_time():
        return datetime.now().strftime("%H:%M:%S")

    msg = "Camera 0: LIVE FEED"
    cv2.putText(img,msg,(10,30),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
    cv2.putText(img,get_time(),(10,60),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)

    
    cv2.imshow("Webcam",img)
    #press esc to exit
    if cv2.waitKey(10) == 27:
        break



webcam.release()
cv2.destroyAllWindows()