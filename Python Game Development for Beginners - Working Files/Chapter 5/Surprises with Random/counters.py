import turtle
from math import sqrt
from time import sleep

counterscreen = turtle.Screen()
counterscreen.reset()

class Counter(turtle.Turtle):
  def __init__(self, coordinates = [160, 170], screen = counterscreen):
    turtle.Turtle.__init__(self)
    self.reset()
    self.hideturtle()
    self.penup()
    self.speed(0)
    x, y = coordinates
    self.goto(x,y)
    self.screen = screen
  def show(self, message, alignment = "right", size = 18):
    self.screen.tracer(0)
    self.clear()
    self.write(message,font=("Arial",size),align=alignment)
    self.screen.tracer(1)
  
class Score(Counter):
  def __init__(self, points=0):
    Counter.__init__(self, coordinates = [160, -170]) 
    self.score = points
    self.update(self.score)
  def update(self, points):
    self.score = points
    self.show("Score: " + str(self.score))
    
class Timer(Counter):
  def __init__(self, time=0):
    Counter.__init__(self)
    self.seconds = time
    self.first = True
  def showtime(self, tick):
    if self.first:
      self.first = False
    else:
      self.seconds = self.seconds + tick
      time = int(round(self.seconds,0))
      self.show("Time: " + str(time))
