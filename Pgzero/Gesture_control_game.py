import pgzrun                       # for GAMING 
from random import randint          # for placing enemy randomly on Screen
import cv2                          # for CAPTURING VIDEO from Camera
import mediapipe as mp              # for HAND DETECTION / KEY POINTS / LOGIC
import sys                          # for CLOSING application

# Game window size according to BACKGROUND IMAGE and CAMERA WINDOW size 
HEIGHT =500
WIDTH = 600


# Creating objects of classes of mediapipe 
# objects name | library name . class name
mp_drawing = mp.solutions.drawing_utils 
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands


cap = cv2.VideoCapture(0)                   # VideoCapture is a function of OpenCV which would help stream or display the video. 0 is index for CAMERA 1 in case of multiple cameras
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 600)      # WIDTH of Camera Window
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 500)     # HEIGHT of Camera Window


hands = mp_hands.Hands(model_complexity=1, min_detection_confidence=0.6, min_tracking_confidence=0.5)

'''
    detection confidence ranges between 0 to 1 (0.5 means 50%) it defines how effectively AI will recognoze the hands
    0 - it will not detect until it is very very sure it is a hand 
    1 - it will reconize anything which looks like a hand this is too much so for optimal we take 0.5
    min_tracking _confidence is the confidence associated with placing the keypoints on hand
    Complexity of the hand detection model: 0, 1 or 2

'''

music.play("ironmantheme")
p = Actor("ironman", pos=(100,100))
c = Actor("thanos2",)
bg = Actor("resize")

# Placing c (thanos2) randomly on screen everytime we run our code
c.x = randint(64, WIDTH-64)
c.y = randint(64, HEIGHT-64)
score = 0                       # score initialized to zero
speed = 10                      # speed of ironman


def draw():
    screen.clear()
    bg.draw()
    p.draw()
    c.draw()
    screen.draw.text(f'score:{score}',{WIDTH-80,10},color="red", gcolor="purple")


def on_mouse_down(pos, button):
    if button == mouse.LEFT and p.collidepoint(pos):
        sounds.i.play()
        print("I am Ironman")
    elif button == mouse.LEFT and c.collidepoint(pos):
        sounds.t.play()
        print("Thanos laugh")

def update():

    # For Keyboard Controls
    player_control()
    update_score()

    if cap.isOpened():                              # If camera is opened
        success, image = cap.read()                 # read image from camera
        if not success:
            print("Ignoring empty camera frame.")
        image.flags.writeable = False                    # making image immutable(unwritable) in memory for less memory consumption and faster processing
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)   # Converting colors - because OpenCV uses BGR an and our mediapipe uses RGB
        results = hands.process(image)                   # sending image in hands model, it will detect hands and store in results
        image.flags.writeable = True                     # making image Mutable again
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)   # Reverting Colors else color will appear all blueish
        width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)        
        height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

        if results.multi_hand_landmarks:                            # If multiple hands are detected
            for hand_landmarks in results.multi_hand_landmarks:     # hands_landmarks me ek ek karke hands leke ao from results.multi_hand_landmarks
                mp_drawing.draw_landmarks(
                    image,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style())
                data = hand_landmarks.landmark[8]
                coords = mp_drawing._normalized_to_pixel_coordinates(data.x, data.y, width, height)
                cv2.circle(image, coords, 10, (0, 255, 255), -1)
                print(coords)
                try:
                    p.center = (WIDTH-coords[0], coords[1])
                except Exception as e:
                    print(e)
        cv2.flip(image, -1)
        cv2.line(image, (0,350), (640,350), (255, 255, 255), 2)
        cv2.putText(image, "OPENCV + PYGAME + MEDIAPIPE", (640//3, 400), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2)
        cv2.imshow('MediaPipe Hands', image)
        if cv2.waitKey(5) & 0xFF == 27:
            cap.release()
            cv2.destroyAllWindows()
            sys.exit()

def update_score():
    global score
    if p.colliderect(c):
        sounds.shoot.play()
        score += 1
        c.pos = (randint(64,WIDTH-64),randint(64,HEIGHT-64))
        x = randint(0,6)
       
        if x==0:
            sounds.t.play()
        else:
            print()






def player_control():
    print("updating")
    if keyboard.RIGHT and not p.right > WIDTH:
        p.angle=-10
        p.x += speed
    elif keyboard.LEFT and not p.left < 0:
        p.x += -speed
        p.angle=10
    elif keyboard.DOWN and not p.bottom > HEIGHT:
        p.y += speed
    elif keyboard.UP and not p.top < 0:
        p.y -= speed
    else:
        p.angle = 0

#outside function the fuction
pgzrun.go()