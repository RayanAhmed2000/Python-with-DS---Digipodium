# Using Classes in Pgzrun
import pgzrun

HEIGHT = 500
WIDTH  = 500

class Player(Actor):
    speed = 3
    
    def move(self):
        if keyboard.LEFT and self.left >0:
            self.x-=self.speed
        if keyboard.RIGHT and self.right <WIDTH:
            self.x+=self.speed


p= Player('ironman', pos=(100,100))

def draw():
    screen.clear()
    p.draw()

def update():
    p.move()

print(dir(Player))              #dir shows all functions in player Since we have actor inherited in Class player, class Player will now have all functions of Actor

pgzrun.go()
