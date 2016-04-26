# import the turtle module so we can use all the neat code it contains
import turtle
from helpercode import BoxTurtle, printwin, checkpos, maketurtles
from time import sleep
from random import randint, choice

# Create variables to contain our BoxTurtle objects
boxturtles = maketurtles(10)

# Create a variable `tina` that is a Turtle() object. Set shape to 'turtle'
tina = turtle.Turtle()
tina.shape('turtle')
tina.penup()

# Create a variable `screen`, a Screen() object, that will handle keyss
screen = turtle.Screen()
screen.bgcolor('lightgreen')

# Keyboard controls
def go_left():
  tina.left(11)
  
def go_right():
  tina.right(11)
  
# Check intersections with boxes when the turtle moves
def go_forward():
  tina.forward(10)
  check_intersect()
  checkpos([tina])

def go_backward():
  tina.backward(10)
  check_intersect()
  checkpos([tina])
  
# This function loops through the `boxes` list and uses each 
# box's `intersect()` method to check whether it intersects
# with tina.
def check_intersect():
  for box in boxturtles:
    if not box.hit and box.intersect(tina):
      box.hit = True
      box.flash()

  
# Tell the program which functions go with which keys
screen.onkey(go_left, 'Left')
screen.onkey(go_right, 'Right')
screen.onkey(go_forward, 'Up')
screen.onkey(go_backward, 'Down')

# This play function will call itself every .1 seconds and return if the player loses
def play():
  # Tell the screen to listen for key presses
  screen.listen()
  # Check boxes' hit state
  hits = []
  for box in boxturtles:
    hits.append(box.hit)
  # If all boxes are hit, the game is over!
  if False not in hits:
    printwin(tina)
    return
  mover = choice(boxturtles)
  if not mover.hit:
    mover.move()
  checkpos(boxturtles)
  # start the function over in 100 miliseconds (.1 seconds)
  screen.ontimer(play, 100)

play() 
turtle.done()