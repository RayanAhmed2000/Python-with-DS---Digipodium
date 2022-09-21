import pgzrun
from random import randint

HEIGHT =500
WIDTH = 600

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
    screen.draw.text(f'score:{score}',{WIDTH-80,10},color = "red")


def update():
    player_control()
    update_score()

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