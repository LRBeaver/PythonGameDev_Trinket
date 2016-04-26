# import the turtle module so we can use all the neat code it contains
import turtle
from helpercode import BoxTurtle, printwin, checkpos, maketurtles
from time import sleep
from random import randint, choice
from levels import make_levels
from counters import Level, Score
 
# Create a variable `tina` that is a Turtle() object. Set shape to 'turtle'
tina = turtle.Turtle()
tina.shape('turtle')
tina.penup()

# Create a variable `screen`, a Screen() object, that will handle keyss
screen = turtle.Screen()
screen.bgcolor('lightgreen')

game_levels = make_levels(4)
level_index = 0
boxturtles = []

levelcounter = Level(0)
scorecounter = Score(0)
  
def setup_level(level, screen):
  n = level["number_turtles"]
  max_speed = level["box_minspeed"]
  min_speed = level["box_maxspeed"]
  global boxturtles
  boxturtles = []
  boxturtles = maketurtles(n, max_speed, min_speed)

setup_level(game_levels[level_index], screen)

# Keyboard controls
def go_left():
  tina.left(11)
  
def go_right():
  tina.right(11)
  
# Check intersections with boxes when the turtle moves
def go_forward():
  tina.forward(10)
  check_intersect(tina.pos(), 20)
  checkpos([tina])

def go_backward():
  tina.backward(10)
  check_intersect(tina.pos(), 20)
  checkpos([tina])
  
# This function loops through the `boxes` list and uses each 
# box's `intersect()` method to check whether it intersects
# with tina.
def check_intersect(coords, radius):
  for box in boxturtles:
    screen.tracer(0)
    if not box.hit and box.intersect(coords, radius):
      box.hit = True
      screen.tracer(1)
      box.flash()
      screen.tracer(0)
  screen.tracer(1)
      
# Power ups!
def boom():
  x, y = tina.pos()
  tina.dot(boomradius)
  tina.color("white")
  check_intersect([x,y], boomradius * 1.1)
  tina.color("black")
  tina.clear()
  
screen.onkey(boom,'b')

# Tell the program which functions go with which keys
screen.onkey(go_left, 'Left')
screen.onkey(go_right, 'Right')
screen.onkey(go_forward, 'Up')
screen.onkey(go_backward, 'Down')

# Debugging function
def win():
  for t in boxturtles[1:]:
    screen.tracer(0)
    t.flash()
    t.hit = True
    screen.tracer(1)

screen.onkey(win, 'w')

# This play function will call itself every .1 seconds and return if the player loses
def play():
  # Tell the screen to listen for key presses
  screen.listen()
  global level_index 
  # Check boxes' hit state
  hits = []
  for box in boxturtles:
    hits.append(box.hit)
  scorecounter.update(hits.count(True))
  # Boomradius
  boomradius = (hits.count(True)+1) * game_levels[level_index]["box_minspeed"] * 1.5
  mover = choice(boxturtles)
  if not mover.hit:
    mover.move()
  # Sometimes,a turtle will awaken
  else:
    if randint(0,1500) < level_index * len(boxturtles):
      mover.awaken()
   # If all boxes are hit, the game is over!
  if False not in hits:
    for box in boxturtles:
      box.hideturtle()
    level_index += 1
    if level_index < len(game_levels):
      # Save score
      scorecounter.total += hits.count(True)
      tina.clear()
      turtle.hideturtle()
      turtle.penup()
      turtle.write(game_levels[level_index]['title'], font = ("Arial", 30), align = "center")
      sleep(2)
      turtle.clear()
      # Next level
      setup_level(game_levels[level_index], screen)
      # Update level display
      levelcounter.update(level_index)
    else:
      printwin()
      return

  checkpos(boxturtles)
  # Vary loop speed with number of turtles
  screen.ontimer(play, 200/len(boxturtles))
  
play()

def printwin():
  turtle.hideturtle()
  turtle.penup()
  turtle.write("You win!", font = ("Arial", 30), align = "center")
  turtle.goto(0,-50)
  turtle.write("Total Score: %d" %(scorecounter.total), font = ("Arial", 18), align = "center")

turtle.done()