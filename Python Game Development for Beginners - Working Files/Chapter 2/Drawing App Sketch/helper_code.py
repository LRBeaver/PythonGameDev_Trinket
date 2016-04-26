import turtle
import random

class GlowTurtle(turtle.Turtle):
  def __init__(self):
    turtle.Turtle.__init__(self)
    self.pencolor("red")
    self.pencolors = ["red","goldenrod", "purple", "pink"]
    self.fillcolors = ["yellow", "black"]
  def glow(self,x,y):
    self.fillcolor(self.fillcolors[0])
  def unglow(self,x,y):
    self.fillcolor(self.fillcolors[1])
  def new_color(self):
    self.color(random.choice(self.pencolors))