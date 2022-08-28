import pgzrun
HEIGTH =500
WIDTH = 600
p = Actor("ironman", pos=(100,100))
speed = 5


def draw():
    screen.clear()
    p.draw()

def update():
    player_control()


def player_control():
    print("updating")
    if keyboard.RIGHT and not p.right > WIDTH:
        p.x += speed
    elif keyboard.LEFT and not p.left < 0:
        p.x += -speed
    elif keyboard.DOWN and not p.bottom > HEIGTH:
        p.y += speed
    elif keyboard.UP and not p.top < 0:
        p.y += -speed
    else:
        p.angle = 0

#outside function the fuction
pgzrun.go()