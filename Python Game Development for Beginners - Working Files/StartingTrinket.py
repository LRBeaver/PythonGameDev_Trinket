import turtle
import random

tina = turtle.Turtle()
tina.shape('turtle')

screen = turtle.Screen()

def on_screen_click(x,y):
    screen.tracer(0)
    tina.goto(x,y)
    screen.bgcolor(random.choice(['white', 'ornage','pink']))
    screen.tracer(1)

screen.onclick(on_screen_click)

screen.listen()
turtle.done()