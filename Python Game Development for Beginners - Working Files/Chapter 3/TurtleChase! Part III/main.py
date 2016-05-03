import turtle
from helpercode import checkpos, intersect, Counter

screen = turtle.Screen()

class Runner(turtle.Turtle):
  def __init__(self):
    turtle.Turtle.__init__(self)
    self.shape('turtle')
    self.penup()
    screen.tracer(10)
    self.setpos(-100,0)
    self.seth(0)
    self.pendown()
    screen.tracer(1)
  def reset(self):
    self.hideturtle()
    self.clear()
    self.__init__()

# A list of all of our chasers
chasers = []

class Chaser(turtle.Turtle):
  def __init__(self, target, coordinates = [100,0]):
    turtle.Turtle.__init__(self)
    self.target = target
    self.coordinates = coordinates
    self.shape('turtle')
    self.color('red')
    self.penup()
    screen.tracer(0)
    self.setpos(coordinates)
    self.seth(self.towards(target))
    self.pendown()
    screen.tracer(1)
    # Add Self to list of Chasers
    if self not in chasers:
      chasers.append(self)
  def reset(self):
    self.hideturtle()
    self.clear()
    self.__init__(self.target, self.coordinates)
  def track(self, move=False):
    screen.tracer(0)
    self.seth(self.towards(self.target))
    if intersect(self.target,self):
      self.write("tag!")
    elif move:
      self.forward(9)
    else:
      self.forward(1)
    checkpos([self.target,self],screen)
    screen.tracer(1)

tina = Runner()
tommy = Chaser(tina)
sally = Chaser(tina, [0,100])
johnny = Chaser(tina, [0,-100])
george = Chaser(tina, [-150,0])

tag_counter = Counter()
tag_counter.showcount()
tag_counter.showcount()

# Reset the game to original state
def reset():
  tina.reset()
  for chaser in chasers:
    chaser.reset()

def chase(move=False):
  for chaser in chasers:
    chaser.track(move)

# Define functions for each arrow key
def go_left():
  screen.tracer(0)
  tina.left(7)
  chase()

  
def go_right():
  screen.tracer(0)
  tina.right(7)
  chase()
  
def go_forward():
  screen.tracer(0)
  tina.forward(10)
  chase(move=True)
  
def go_backward():
  screen.tracer(0)
  tina.backward(10)
  chase(move=True)
  
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