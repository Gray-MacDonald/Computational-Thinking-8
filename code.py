import codesters
import random

# Setup the stage
stage = codesters.Stage()
stage.set_background("summer")

# Create the player (cheesepizza sprite)
player = codesters.Sprite("cheesepizza")
player.set_size(0.1)
player.set_position(0, -200)

# Initialize the score
score = 0
score_display = codesters.Text(score, 0, 200)

# Function to create falling pepperonis
def create_pepperoni():
    x = random.randint(-250, 250)  # Random x position
    y = 250  # Start at the top of the screen
    pepperoni = codesters.Sprite("pepp", x, y)
    pepperoni.set_y_speed(-5)  # Move downward
    return pepperoni

# Create new pepperonis at regular intervals
stage.event_interval(create_pepperoni, 1)

# Function to check collision with pepperonis
def check_collision():
    global score
    for pepperoni in stage.get_sprites():
        if pepperoni.get_image_name() == "pepp":
            if player.is_touching(pepperoni):
                score += 1  # Increase score
                score_display.set_text(score)
                stage.remove_sprite(pepperoni)  # Remove the caught pepperoni

# Function to move player left
def move_left():
    player.move_left(10)

# Function to move player right
def move_right():
    player.move_right(10)

# Key events to move player
player.event_key("left", move_left)
player.event_key("right", move_right)

# Event to check for collisions
stage.event_interval(check_collision, 0.1)
