import random
import pgzrun


WIDTH = 612
HEIGHT = 408
MAX_BULLETS = 3

level = 1
lives = 3
score = 0

bg = Actor("town",center =(305,203))
#p = Actor("player", (200, 580))
enemies = []
bullets = []
bombs = []

def draw():
    bg.draw()

pgzrun.go()