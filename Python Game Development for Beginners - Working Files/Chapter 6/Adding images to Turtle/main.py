import turtle

screen = turtle.Screen()

# this assures that the size of the screen will always be 400x400 ...
screen.setup(400, 400)

# ... which is the same size as our image
# now set the background to our space image
screen.bgpic("starfield.gif")

# Or, set the shape of a turtle
# Note: Python (as opposed to Trinket) doesn't allow for rotation of
# image-shaped turtles. So I commented out these two lines:
#screen.addshape("rocketship.gif")
#turtle.shape("rocketship.gif")

# Instead I made a light grey turtle as our spaceship:
turtle.shape("turtle")
turtle.color("lightgrey")

move_speed = 10
turn_speed = 10

# these defs control the movement of our "turtle"
def forward():
  turtle.forward(move_speed)

def backward():
  turtle.backward(move_speed)

def left():
  turtle.left(turn_speed)

def right():
  turtle.right(turn_speed)

turtle.penup()
turtle.speed(0)
turtle.home()

# now associate the defs from above with certain keyboard events
screen.onkey(forward, "Up")
screen.onkey(backward, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")
screen.listen()
turtle.done()
