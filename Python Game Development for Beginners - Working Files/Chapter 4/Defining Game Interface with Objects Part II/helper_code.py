import turtle
from math import sqrt
from time import sleep

screen = turtle.Screen()
screen.reset()
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
    screen.tracer(0)
    self.setpos(x,y)
    screen.tracer(1)
    
  def intersect(self, object):
    xbounds = (self.xcor()-self.radius, self.xcor() + self.radius)
    ybounds = (self.ycor()-self.radius, self.ycor() + self.radius)
    x, y = object.pos()
    check_x = x > min(xbounds) and x < max(xbounds)
    check_y = y > min(ybounds) and y < max(ybounds)
    if (check_x and check_y):
      return True
    else:
      return False
      
  def flash(self):
    for i in range(10):
      self.color('red')
      self.color('yellow')
    return
  
def printwin(turtle, time, score):
  turtle.hideturtle()
  turtle.penup()
  turtle.goto(0,15)
  turtle.color("green")
  turtle.write("You Win!",font=("Arial",30), align = "center")
  turtle.goto(0,-50)
  turtle.write("Score: %d  Time: %d" %(score.score, time), font=("Arial",15), align = "center")