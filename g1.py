from ctypes.wintypes import SIZE
import pgzrun

HEIGHT = 600
WIDTH = 600

p = Actor('iron',pos=(250,300))

def draw():
    screen.clear()
    screen.draw.text("Welcome to pgzero",(20,10),color='red',fontsize=60)
    screen.draw.text("Created by Rayan",(60,50),color='White')
    p.draw()

pgzrun.go()