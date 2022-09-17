import pgzrun
from random import randint          # for 
import cv2                          # computer vision library
import mediapipe as mp
import sys


HEIGHT =500
WIDTH = 600


mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands


cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# box = Rect((0, 250,), (10,10))
hands = mp_hands.Hands(model_complexity=0, min_detection_confidence=0.5, min_tracking_confidence=0.5)

music.play("ironmantheme")
p = Actor("ironman", pos=(100,100))
c = Actor("thanos2",)
c.x = randint(64, WIDTH-64)
c.y = randint(64, HEIGHT-64)
score = 0
speed = 5


def draw():
    screen.clear()
    p.draw()
    c.draw()
    screen.draw.text(f'score:{score}',{WIDTH-80,10})

def update():
    player_control()
    update_score()
    if cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
        image.flags.writeable = False
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = hands.process(image)
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
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
        cv2.flip(image, 1)
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