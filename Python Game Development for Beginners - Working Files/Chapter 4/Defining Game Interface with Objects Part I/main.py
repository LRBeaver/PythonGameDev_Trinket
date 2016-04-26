import turtle

counterscreen = turtle.Screen()

class Counter(turtle.Turtle):
  def __init__(self, coordinates = [160, 170], screen = counterscreen):
    turtle.Turtle.__init__(self)
    self.count = 0
    self.hideturtle()
    self.screen = screen
  def show(self, message, alignment = "right", size = 18):
    self.screen.tracer(0)
    self.clear()
    self.write(message,font=("Arial",size),align=alignment)
    self.screen.tracer(1)
  def increment(self):
    self.count += 1
  def showcount(self, x, y):
    self.increment()
    self.show(self.count)
    
clicks_counter = Counter()

counterscreen.onclick(clicks_counter.showcount)
turtle.done()