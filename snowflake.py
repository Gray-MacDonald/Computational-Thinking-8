import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("sky blue")

# Create a turtle for drawing
snowflake = turtle.Turtle()
snowflake.shape("turtle")
snowflake.color("white")
snowflake.speed(0)  # Set the speed to the fastest

# Function to draw the Koch curve (a fractal)
def koch_curve(t, order, length):
    if order == 0:
        t.forward(length)
    else:
        length /= 3.0
        koch_curve(t, order - 1, length)
        t.left(60)
        koch_curve(t, order - 1, length)
        t.right(120)
        koch_curve(t, order - 1, length)
        t.left(60)
        koch_curve(t, order - 1, length)

# Function to draw a snowflake using Koch curve
def koch_snowflake(t, order, length):
    for _ in range(3):  # A snowflake has 3 sides
        koch_curve(t, order, length)
        t.right(120)

# Position the turtle
snowflake.penup()
snowflake.goto(-150, 90)
snowflake.pendown()

# Draw the detailed snowflake
koch_snowflake(snowflake, order=4, length=300)  # Increase order for more detail

# Hide the turtle after drawing
snowflake.hideturtle()

# Keep the window open
turtle.done()
