import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle object
star_turtle = turtle.Turtle()
star_turtle.shape("turtle")
star_turtle.color("black")
star_turtle.speed(3)

# Function to draw a 5-pointed star
def draw_star(size):
    for i in range(5):
        star_turtle.forward(size)  # Move forward by the given size
        star_turtle.right(144)      # Turn by 144 degrees to create the star

# Position the turtle to start drawing
star_turtle.penup()
star_turtle.goto(-50, 0)
star_turtle.pendown()

# Draw the star
draw_star(100)

# Hide the turtle and finish
star_turtle.hideturtle()

# Keep the window open
turtle.done()
