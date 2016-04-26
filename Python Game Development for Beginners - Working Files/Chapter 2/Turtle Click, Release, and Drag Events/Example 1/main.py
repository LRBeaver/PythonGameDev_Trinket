import turtle
from helper_code import ToggleTurtle

# Create a variable `tina` that is a Turtle() object. Set shape to 'turtle'
tina = ToggleTurtle()
tina.shape('turtle')

tina.onclick(tina.toggle_color)

turtle.done()