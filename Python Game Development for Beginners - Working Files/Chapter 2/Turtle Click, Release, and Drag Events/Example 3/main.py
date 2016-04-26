import turtle

tina = turtle.Turtle()
tina.shape('turtle')

screen = turtle.Screen()

def on_drag_function(x,y):
  screen.tracer(0)
  tina.goto(x,y)
  screen.tracer(1)

tina.ondrag(on_drag_function)

turtle.done()