from textwrap import fill
from turtle import *

speed('slowest')
pencolor('blue')
bgcolor('white')
width(3)


side= 3
size= 200
fillcolor("green")
begin_fill()
for i in range(side):
    fd(size)
    lt(360/side)
end_fill()
mainloop()