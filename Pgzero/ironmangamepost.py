import pgzrun
from random import randint

HEIGHT = 608
WIDTH = 1136


music.play("ironmantheme")

p = Actor("ironman", pos=(100,100))
c = Actor("thanos2", pos=(150,100))
bg = Actor("bgimg")


c.x = randint(64, WIDTH-64)
c.Y = randint(64, HEIGHT-64)

score = 0
speed = 5

def draw():
    screen.clear()
    bg.draw()
    p.draw()
    c.draw()
    screen.draw.text(f'score:{score}',{WIDTH-80,10})

def update_score():
    global score
    if p.colliderect(c):
        score+=1
        sounds.shoot.play()
        c.pos = (randint(64,WIDTH-64),randint(64,HEIGHT-64))



def update():
    player_control()
    update_score()



def player_control():
    print("Running")
    if keyboard.RIGHT and not p.right >WIDTH:
        p.angle = -10
        p.x+=speed
    elif keyboard.LEFT and not p.left <0:
        p.angle = 10
        p.x-=speed
    elif keyboard.DOWN and not p.bottom>HEIGHT:
        p.y+=speed
    elif keyboard.UP and not p.top<0:
        p.y-=speed
    else:
        p.angle = 0

pgzrun.go()
    