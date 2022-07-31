from turtle import *

 #to do it with loop we will save our pattern points in a list 

c=[(-300,300),(0,300),(300,300),
   (-150,150),(150,150),
   (0,0)
   ]
speed("fastest")

penup()
for i in range(6):
    goto(c[i])
    pendown()
    dot(50)
    penup()
mainloop()