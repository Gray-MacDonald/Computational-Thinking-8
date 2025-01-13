import turtle
import random

t = turtle.Turtle()
# speed so it will make the picture faster
t.speed(10)

colors = ['red','blue','green','black','yellow','orange','dark gray']
angles =[90,180,270,360]
for i in range(100000):
    t.color( colors[i%6])
    t.forward(10)
    t.left(random.choice(angles))

turtle.exitonclick()