import pgzrun
from random import randint

HEIGHT =500
WIDTH = 600

p = Actor("ironman", pos=(100,100))

speed = 1


def draw():
    screen.clear()
    p.draw()

def update():
    player_control()


def player_control():
    print("Moving")
    for i in range(0,10):
        p.y+=randint(1,15)
        p.y-=randint(1,15)

pgzrun.go()
