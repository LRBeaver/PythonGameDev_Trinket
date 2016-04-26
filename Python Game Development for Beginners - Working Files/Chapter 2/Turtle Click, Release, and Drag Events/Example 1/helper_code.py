import turtle

class ToggleTurtle(turtle.Turtle):
  def __init__(self):
    turtle.Turtle.__init__(self)
    self.color_1 = 'grey'
    self.color_2 = 'green'
    self.fillcolor(self.color_1)
    self.pencolor(self.color_2)
  def toggle_color(self, x, y):
    colors = self.color()
    self.color(colors[1], colors[0])