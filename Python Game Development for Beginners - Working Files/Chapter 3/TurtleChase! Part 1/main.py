import turtle
from helpercode import checkpos, intersect, Counter

screen = turtle.Screen()

class Runner(turtle.Turtle):
  def __init__(self):
    turtle.Turtle.__init__(self)

class Chaser(turtle.Turtle):
  def __init__(self):
    turtle.Turtle.__init__(self)

tina = Runner()
tommy = Chaser()

# Put the turtles in original positions
def start():
  tina.shape('turtle')
  tommy.shape('turtle')
  tommy.color('red')
  tina.penup()
  tommy.penup()
  screen.tracer(10)
  tina.setpos(-100,0)
  tommy.setpos(100,0)
  tina.seth(0)
  tommy.seth(tommy.towards(tina))
  tina.pendown()
  tommy.pendown
  screen.tracer(1)
  
start()

# Reset the game to original state
def reset():
  tina.reset()
  tommy.reset()
  start()

# A function so tommy can track tina
def track(move=False):
  tommy.seth(tommy.towards(tina))
  if intersect(tina,tommy):
    tommy.write("tag!")
  elif move:
    tommy.forward(9)
  else:
    tommy.forward(1)
  checkpos([tina,tommy],screen)
  screen.tracer(1)

# Define functions for each arrow key
def go_left():
  screen.tracer(0)
  tina.left(7)
  track()
  
def go_right():
  screen.tracer(0)
  tina.right(7)
  track()
  
def go_forward():
  screen.tracer(0)
  tina.forward(10)
  track(move=True)
  
def go_backward():
  screen.tracer(0)
  tina.backward(10)
  track(move=True)
  
# Tell the program which functions go with which keys
screen.onkey(go_left, 'Left')
screen.onkey(go_right, 'Right')
screen.onkey(go_forward, 'Up')
screen.onkey(go_backward, 'Down')

# Reset the game when the user presses 'r'
screen.onkey(reset,"r")

# Tell the screen to listen for key presses
screen.listen()
turtle.done()