
# import the turtle module so we can use all the neat code it contains
import turtle

# Create a variable `tina` that is a Turtle() object. Set shape to 'turtle'
tina = turtle.Turtle()
tina.shape('turtle')

# Create a variable `screen`, a Screen() object, that will handle clicks
screen = turtle.Screen()

# Define a simple function that tells our turtle to go to x,y coordinates
def on_screen_click(x, y):
  screen.tracer(0)
  tina.goto(x, y)
  screen.tracer(1)
    
# when the screen is clicked, run the `on_screen_click` function. 
# The x and y coordinates are passed along to the function.
screen.onclick(on_screen_click)
turtle.done()
