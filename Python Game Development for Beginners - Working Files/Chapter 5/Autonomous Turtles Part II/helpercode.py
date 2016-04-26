import turtle
from math import sqrt
from time import sleep
from random import randint

screen = turtle.Screen()
screen.register_shape("box",((-10,10),(10,10),(10,-10),(-10,-10)))
screen.register_shape("hidingturtle",([0,10],[-2,10],[-1,10],[-4,7],[-6,5],[-7,1],[-5,-3],[-4,-5],[0,-7],[4,-5],[5,-3],[7,1],[6,5],[4,7],[1,10]))

class BoxTurtle(turtle.Turtle):
  # Override some defaults:
  def __init__(self):
    turtle.Turtle.__init__(self)
    self.speed(3)
    self.penup()
    self.shape("turtle")
    self.color("brown")
    # Give them a random starting location
    self.setpos(randint(-200,200),randint(-200,200))
    # Give them a random orientation
    self.seth(randint(0,360))
    self.radius = 20
    self.hit = False
    
  def place(self, x, y):
    self.setpos(x,y)
    
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
    for i in range(3):
      self.color('green')
      self.color('yellow')
      self.color('brown')
      self.shape('hidingturtle')
    return
  
  def move(self):
    if randint(0,1) == 1:
      self.seth(self.heading() + randint(-45,45))
    self.forward(randint(3,20))
  
def printwin(turtle):
  turtle.stamp()
  turtle.hideturtle()
  turtle.penup()
  turtle.goto(0,0)
  turtle.color("green")
  turtle.write("You Win!",font=("Arial",30), align = "center")
  
def checkpos(turtlelist):
  screen.tracer(0)
  for turtle in turtlelist:
    x = turtle.xcor()
    y = turtle.ycor()
    if x > 200:
      turtle.setx(-200)
    elif x < -200:
      turtle.setx(200)
    if y > 200:
      turtle.sety(-200)
    elif y < -200:
      turtle.sety(200)
  screen.tracer(1)
  return

def maketurtles(n = 10):
  screen.tracer(0)
  boxturtles = []
  for i in range(n):
    newturtle = BoxTurtle()
    boxturtles.append(newturtle)
  screen.tracer(1)
  return boxturtles