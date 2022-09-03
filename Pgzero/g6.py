import pgzrun
from random import randint

HEIGHT = 330
WIDTH = 523

speed = 7    # player speed
es = 1        # enemy speed



game_over = False           # switch   
game_started = False        # switch

center=(WIDTH//2,HEIGHT//2)# points to center coordinates
bg = Actor('bg', center =(259,167)) 
p = Actor('ironman', pos =(100,100))   
e = Actor("thanos2" , pos =(200,100))


def show_screen1():
    bg.draw()
    #screen.fill('#ffff00')
    screen.draw.text('Ironman - The Game',center=center,fontsize = 60, color = 'white')
    screen.draw.text('press space to start', center = (center[0],center[1]+100), fontsize = 50, color = 'white')

def show_game_screen():
    bg.draw()
    p.draw()
    e.draw()
   
def draw():
    screen.clear()
    if not game_started:
        show_screen1()
    elif game_started and not game_over:
        show_game_screen()
    elif game_over:
        show_game_over()    
    
def show_game_over():
    bg.draw()
    screen.draw.text('Game Over',center=center,fontsize = 100, color = 'white')




def update():
    global game_started

    if keyboard.SPACE and not game_started:
      game_started = True
      bg.image='bg'

    if game_started and not game_over:
        player_control()
        enemy_control()
 
            

    
    

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

def enemy_control():
    global game_over
    if p.x>e.x:
        e.x += es
    if p.x<e.x:
        e.x -=es
    if p.y>e.y:
        e.y += es
    if p.y<e.y:
        e.y -=es
    if p.colliderect(e):
        game_over = True
        sounds.eating2.play()

pgzrun.go()