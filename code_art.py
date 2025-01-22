import turtle
import random
#start
t = turtle.Turtle()
# speed so it will make the picture faster
t.speed(0)

colors = ['red','blue','green','black','orange','dark gray']
#random angles that is will turn to make boxes
angles =[90,180,270,360]
for i in range(100000):
    t.color( colors[i%6])
    t.forward(10)
    #make it go at random
    t.left(random.choice(angles))
#so it won't go of the page 
if t.xcor() > 250:
    t.pendup()
    t.goto(0,0)
    t.pendownn()

if t.xcor() > -250:
    t.pendup()
    t.goto(0,0)
    t.pendownn()

if t.ycor() > 250:
    t.pendup()
    t.goto(0,0)
    t.pendownn()

if t.ycor() > -250:
    t.pendup()
    t.goto(0,0)
    t.pendownn()
#so it won't be black when the code is over
#end
turtle.exitonclick()