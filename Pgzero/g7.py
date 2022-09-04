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
        if keyboard.UP and not self.top <0:
            self.y-=self.speed
        if keyboard.DOWN and not self.bottom >HEIGHT:
            self.y+=self.speed

class Enemy(Actor):
    speed = 1
    
    def chase(self):
        if p.x>e.x:
            e.x += self.speed
        if p.x<e.x:
            e.x -=self.speed
        if p.y>e.y:
            e.y += self.speed
        if p.y<e.y:
            e.y -=self.speed
        if p.colliderect(e):
            print("collision")
        

p= Player('ironman', pos=(100,100))
e= Enemy("thanos2" , pos =(200,400))

def draw():
    screen.clear()
    p.draw()
    e.draw()

def update():
    p.move()
    e.chase()

print(dir(Player))              #dir shows all functions in player Since we have actor inherited in Class player, class Player will now have all functions of Actor

pgzrun.go()
