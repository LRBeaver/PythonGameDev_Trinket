# import the turtle module so we can use all the neat code it contains
import turtle
from helper_code import GlowTurtle

# Create a variable `tina` that is a Turtle() object. Set shape to 'turtle'
tina = GlowTurtle()
tina.shape('turtle')

# Create a variable `screen`, a Screen() object, that will handle keyss
screen = turtle.Screen()

# tina is a GlowTurtle (see helper_code.py), so we can
# call the glow and unglow methods on click and release
tina.onclick(tina.glow)     # clicking on turtle turns fillcolor red,
tina.onrelease(tina.unglow) # releasing turns it to transparent.

# Define a function for each arrow key
def go_left():
  tina.left(7)
  
def go_right():
  tina.right(7)
  
def go_forward():
  tina.forward(10)
  
def go_backward():
  tina.backward(10)
  
# Tell the program which functions go with which keys
screen.onkey(go_left, 'Left')
screen.onkey(go_right, 'Right')
screen.onkey(go_forward, 'Up')
screen.onkey(go_backward, 'Down')

# Call the new_color method when 'c' is presssed
screen.onkey(tina.new_color, 'c')

# Define a function for drags
def on_drag_function(x,y):
  screen.tracer(0)
  tina.goto(x,y)
  screen.tracer(1)

# Call that function when tina s dragged
tina.ondrag(on_drag_function)

# Define a simple function that tells our turtle to go to x,y coordinates
def on_screen_click(x, y):
  screen.tracer(0)
  tina.goto(x, y)
  screen.tracer(1)
  
# when the screen is clicked, run the `on_screen_click` function. 
# The x and y coordinates are passed along to the function.
screen.onclick(on_screen_click)

# Tell the screen to listen for key presses
screen.listen()

turtle.done()