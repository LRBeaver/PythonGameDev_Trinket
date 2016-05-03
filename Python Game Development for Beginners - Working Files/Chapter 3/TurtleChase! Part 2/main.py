import turtle
from helpercode import checkpos, intersect, Counter

screen = turtle.Screen()

class Runner(turtle.Turtle):
  def __init__(self):
    turtle.Turtle.__init__(self)
    self.shape('turtle')
    self.penup()
    screen.tracer(10)
    self.setpos(-100, 0)
    self.seth(0)
    self.pendown()
    screen.tracer(1)
  def reset(self):
    self.hideturtle()
    self.clear()
    self.__init__()

class Chaser(turtle.Turtle):
  def __init__(self, target):
    turtle.Turtle.__init__(self)
    self.target = target
    self.shape('turtle')
    self.color('red')
    self.penup()
    screen.tracer(10)
    self.setpos(100, 0)
    # Towards where??
    self.seth(self.towards(target))
    self.pendown
    screen.tracer(1)
    def reset(self):
      self.hideturtle()
      self.clear()
      self.__init__()
    def track(self, move=False):
      self.seth(self.towards(self.target))
      if intersect(self.target, self):
        self.write("tag!")
      elif move:
        self.forward(9)
      else:
        self.forward(1)
      checkpos([self.target, self], screen)
      screen.tracer(1)

tina = Runner()
tommy = Chaser(tina)


# A function so tommy can track tina
# def track(move=False):
#   tommy.seth(tommy.towards(tina))
#   if intersect(tina,tommy):
#     tommy.write("tag!")
#   elif move:
#     tommy.forward(9)
#   else:
#     tommy.forward(1)
#   checkpos([tina,tommy],screen)
#   screen.tracer(1)

# Define functions for each arrow key
def go_left():
  screen.tracer(0)
  tina.left(7)
  tommy.track()
  
def go_right():
  screen.tracer(0)
  tina.right(7)
  tommy.track()
  
def go_forward():
  screen.tracer(0)
  tina.forward(10)
  tommy.track(move=True)
  
def go_backward():
  screen.tracer(0)
  tina.backward(10)
  tommy.track(move=True)
  
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