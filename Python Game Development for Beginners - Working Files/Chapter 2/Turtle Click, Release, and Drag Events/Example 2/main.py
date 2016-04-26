import turtle
from helper_code import GlowTurtle

tina = GlowTurtle()
tina.shape("turtle")
tina.onclick(tina.glow)     # clicking on turtle turns fillcolor red,
tina.onrelease(tina.unglow) # releasing turns it to transparent.

turtle.done()