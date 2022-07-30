from turtle import *
pensize(3)

for i in range(4):
    fd(100)
    pencolor('red')
    write(i,font=('Arial',14,'normal'),align='left')
    for j in range(6):
        pencolor('blue')
        fd(60)
        pencolor('red')
        write(j,font=('Arial',14,'normal'),align='left')
        lt(360/6)
    lt(360/4)
mainloop()   
