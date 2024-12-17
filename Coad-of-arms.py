###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################\

stage.set_background("winter")

q1 = codesters.Square(100, 100, 200, 'ForestGreen')
q2 = codesters.Square(-100, 100, 200, 'SkyBlue')
q3 = codesters.Square(-100, -100, 200, 'white')
q4 = codesters.Square(100, -100, 200, 'black')

s1 = codesters.Sprite("basketball", 100, 100)
s1.set_size(1.5)
s2 = codesters.Sprite("skiing", -100, -100)
s2.set_size(0.2)
s3 = codesters.Sprite("dog", 100, -100)
s3.set_size(0.2)
s4 = codesters.Sprite("cardinal", -100, 100)
s4.set_size(1)

message1 = codesters.Text("By Gray",0,220,"red")
message1 = codesters.Text("I have a dog",0,-220,"black")
