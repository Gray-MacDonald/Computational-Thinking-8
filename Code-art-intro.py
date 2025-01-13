# ###############################################
# ### SETUP ###
import turtle
# ###############################################

t = turtle.Turtle()
t.penup()
t.goto(-100, -250)
t.color("purple")
t.pendown()

# t.forward(200)
# t.left(90)
# t.forward(100)
# t.left(90)
# t.forward(200)
# t.left(90)
# t.forward(100)
# t.right(90)

for i in range(360):
    t.forward(1)
    t.left(1)

# ###############################################
# ### ENDING ###
turtle.exitonclick()
# ###############################################
