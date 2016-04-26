import turtle

class GlowTurtle(turtle.Turtle):
  def __init__(self):
    turtle.Turtle.__init__(self)
    self.pencolor("red")
  def glow(self,x,y):
    self.fillcolor("yellow")
  def unglow(self,x,y):
    self.fillcolor("")