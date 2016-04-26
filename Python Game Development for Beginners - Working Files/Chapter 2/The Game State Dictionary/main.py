# import the turtle module so we can use all the neat code it contains
import turtle

# Create a variable `tina` that is a Turtle() object. Set shape to 'turtle'
tina = turtle.Turtle()
tina.shape('turtle')
tina.penup()
tina.goto(0,-100)

# Create a variable `screen`, a Screen() object, that will handle clicks
screen = turtle.Screen()

# Use a dictionary to keep track of state
state = {'clicks': 0} 

# Define a simple function that counts clicks
def on_screen_click(x, y):
  screen.tracer(0)
  state['clicks'] += 1
  tina.clear()
  tina.goto(x, y)
  tina.write("You've clicked %d times" % state['clicks'],font=("Arial",14),align="center")
  tina.goto(x, y-20)
  screen.tracer(1)
  
# when the screen is clicked, run the `on_screen_click` function. 
# The x and y coordinates are passed along to the function.
screen.onclick(on_screen_click)
turtle.done()