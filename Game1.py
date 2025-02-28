#section 1: setup
import codesters 
from codesters import StageClass
stage = StageClass()

stage.set_background("moon")
s1 = codesters.Sprite("person1",0,-200)
s1.set_size(0.5)



#section 2 :define controles 
def move_up(sprite):
    sprite.move_up(10)

def move_down(sprite):
    sprite.move_down(10)

def move_left(sprite):
    sprite.move_left(10)

def move_right(sprite):
    sprite.move_right(10)

def show(sprite):
    sprite.show ()

def turn_left(sprite):
    heading = sprite.heading 
    sprite.set_heading(heading + 1)

def turn_right(sprite):
    heading = sprite.heading 
    sprite.set_heading(heading - 1)

def forward(sprite):
    sprite.forward(1)

def draw(sprite):
    sprite.pen_down()

def stop_drawing(sprite):
    sprite.pen_up()

# Section 3: define hide and show 
def hide(sprite):
    sprite.hide()

def erase(sprite):
    sprite.pen_clear()
    
# section 4: bind contres to specific keys 
s1.event_key ("w", move_up)
s1.event_key ("s", move_down)
s1.event_key ("a", move_left)
s1.event_key ("d", move_right)
s1.event_key ("h", hide)
s1.event_key ("g", show)
s1.event_key ("v", draw)
s1.event_key ("c", stop_drawing)
s1.event_key ("p", erase)
#section 5: reminder message 
print("Game has started. Open the screen using PORTS to play") 

