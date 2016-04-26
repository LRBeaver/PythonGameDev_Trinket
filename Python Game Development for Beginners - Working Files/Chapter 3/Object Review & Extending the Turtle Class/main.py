import turtle

tina = turtle.Turtle()
tina.shape("turtle")

class BoxTurtle(turtle.Turtle):
  def __init__(self):
    turtle.Turtle.__init__(self)

tommy = BoxTurtle()

tommy.shape("turtle")
tommy.sety(-100)
tommy.color("brown")

turtle.done()