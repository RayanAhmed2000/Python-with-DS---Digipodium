from turtle import *

l=int(input("enter the length of side "))
s=int(input("enter the number of sides of polygon "))

for i in range(s):
    forward(l)
    left(360/s)

mainloop()