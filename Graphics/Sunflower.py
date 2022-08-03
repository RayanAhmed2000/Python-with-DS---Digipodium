from turtle import *
pensize(2)
speed('fastest')

size=100
side=10
bgcolor('green')
for i in range(side):
    fillcolor('yellow')
    begin_fill()
    pencolor('black')
    fd(size)
    #write(i,font=('Arial',14,'normal'),align='left')
    for j in range(side):
        #pencolor('blue')
        fd(size//2)
        #pencolor('red')
        #write(j,font=('Arial',14,'normal'),align='left')
        lt(360/side)
    lt(360/side)
    end_fill()
fillcolor('black')
begin_fill()
rt(90)
fd(300)
rt(90)
fd(5)
rt(90)
fd(300)
end_fill()
write("Sunflower",font=('Arial',30,'normal'),align='left')
mainloop()   
