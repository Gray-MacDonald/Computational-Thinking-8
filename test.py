# move to stripe 3
import turtle
t = turtle.Turtle()
h = 10
t.penup()
t.goto(-250, 0)
t.pendown()
# stripe 3
t.color("red")
t.begin_fill()
t.forward(500)
t.left(90)
t.forward(h)
t.left(90)
t.forward(500)
t.left(90)
t.forward(h)
t.left(90)
t.end_fill()

turtle.exitonclick()
