#Section 1-setup
import codesters, random
from codesters import StageClass
stage = StageClass()
stage.disable_floor()
player = codesters.Sprite("cheesepizza")
player.set_size(.09)
stage.set_background("summer")
object_speed = -8
points = 0
lives = 5

# #section 2 Object
def falling_object():
    global object_speed, points, lives
    if lives >=1:
        x = random.randint(-250,250)
        y = 250
        object = codesters.Sprite("pepp",x,y)
        object.set_size(.7)
        object.set_y_speed (object_speed)
stage.event_interval(falling_object,.8)
# section 3
def collision(player,object):
    global lives, object_speed
    if object.get_image_name() == "pepp":
        stage.remove_sprite(object)
        object_speed-=1
        lives-=1
        if lives == 0:
            player.say(f"out of lives - you lose!",5)
        else:
            player.say(f"{lives}lives",0.5)
player.event_collision(collision)

# # section 4
def go_right():
    player.move_right(10)
player.event_key("right", go_right)

def go_left():
    player.move_left(10)
player.event_key("left", go_left)
