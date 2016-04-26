# import the turtle module so we can use all the neat code it contains
import turtle

# Create a variable `tina` that is a Turtle() object. Set shape to 'turtle'
tina = turtle.Turtle()
tina.shape('turtle')

# Create a variable `screen`, a Screen() object, that will handle keyss
screen = turtle.Screen()

# Define a functions for each arrow key
def go_left():
  #screen.tracer(0)
  tina.left(7)
  #screen.tracer(1)
  
def go_right():
  #screen.tracer(0)
  tina.right(7)
  #screen.tracer(1)
  
def go_forward():
  #screen.tracer(0)
  tina.forward(20)
  #screen.tracer(1)
  
def go_backward():
  #screen.tracer(0)
  tina.backward(20)
  #screen.tracer(1)
  
# Tell the program which functions go with which keys
screen.onkey(go_left, 'Left')
screen.onkey(go_right, 'Right')
screen.onkey(go_forward, 'Up')
screen.onkey(go_backward, 'Down')

# Go to where the user clicks
def go(x, y):
  #screen.tracer(0)
  tina.goto(x, y)
  #screen.tracer(1)
  
screen.onclick(go)

# Tell the screen to listen for key presses
screen.listen()
turtle.done()