from textwrap import fill
from turtle import *

speed('slowest')
pencolor('blue')
bgcolor('pink')
width(3)


side= 3
size= 200
for i in range(side):
    fd(size)
    lt(360/side)

mainloop()