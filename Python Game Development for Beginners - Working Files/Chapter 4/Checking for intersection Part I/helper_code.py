import turtle
from math import sqrt
from time import sleep

screen = turtle.Screen()
screen.register_shape("box",((-10,10),(10,10),(10,-10),(-10,-10)))

class Box(turtle.Turtle):
  # Override some defaults:
  def __init__(self,x=0,y=0):
    turtle.Turtle.__init__(self)
    self.speed(0)
    self.penup()
    self.shape("box")
    self.setpos(x,y)
    self.radius = 20
    self.hit = False
    
  def place(self, x, y):
    self.setpos(x,y)
    
  def intersect(self, object):
    print "Checking Intersect"
    # Our code here
    return False
      
  def flash(self):
    # A nice visual indicator that something happened
    for i in range(10):
      self.color('red')
      self.color('yellow')
    return
  
def printwin(turtle):
  turtle.stamp()
  turtle.hideturtle()
  turtle.penup()
  turtle.goto(turtle.xcor(),turtle.ycor() + 15)
  turtle.color("green")
  turtle.write("You Win!",font=("Arial",30), align = "center")