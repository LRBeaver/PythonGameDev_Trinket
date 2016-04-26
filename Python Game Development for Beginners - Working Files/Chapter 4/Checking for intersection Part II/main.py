# import the turtle module so we can use all the neat code it contains
import turtle
from helper_code import Box, printwin
 
# Create variables to contain our Box objects
a = Box(100,100)
b = Box(-100,100)
c = Box(100,-100)
d = Box(-100,-100) 

# Make a list of boxes so we can loop over them and change state
boxes = [a, b, c, d]

# Create a variable `tina` that is a Turtle() object. Set shape to 'turtle'
tina = turtle.Turtle()
tina.shape('turtle')

# Create a variable `screen`, a Screen() object, that will handle keyss
screen = turtle.Screen()

# Keyboard controls
def go_left():
  tina.left(11)
  
def go_right():
  tina.right(11)
  
# Check intersections with boxes when the turtle moves
def go_forward():
  tina.forward(10)
  check_intersect()

def go_backward():
  tina.backward(10)
  check_intersect()
  
# This function loops through the `boxes` list and uses each 
# box's `intersect()` method to check whether it intersects
# with tina.
def check_intersect():
  hits = []
  for box in boxes:
    if not box.hit and box.intersect(tina):
      box.flash()
      box.hit = True
    hits.append(box.hit)
  # If all boxes are hit, the game is over!
  if False not in hits:
    printwin(turtle.Turtle())
  
# Tell the program which functions go with which keys
screen.onkey(go_left, 'Left')
screen.onkey(go_right, 'Right')
screen.onkey(go_forward, 'Up')
screen.onkey(go_backward, 'Down')

# Tell the screen to listen for key presses
screen.listen()
turtle.done()