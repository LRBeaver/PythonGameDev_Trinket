You'll notice that the working files of this chapter are slightly different than
the ones I used in the video.  The while loop I use in the video causes stock
Python to freeze up.  

Instead of the while loop, we use a recursive play() function.  I want to 
explain recursive functions briefly in case you're curious.  They're neat!

Here's the basic format of our main game loop:

```
# This play function will call itself every .1 seconds and return if the player loses
def play():
  
  # Main game goes here
  
  # start the function over in 100 miliseconds (.1 seconds)
  screen.ontimer(play, 100)

play()
```

screen.ontimer basically calls the function you give it in the number of miliseconds 
you specify.  We use it to call the same function, play, from within the function itself.
This is recursion.  To recur means to start over, and that's exactly what happens here.
The main game loop runs once, waits .1 seconds, then starts over. We break this loop
by calling `return` instead of setting `playing = False` like in the video.

This is a more advanced architecture but it's very neat and what I'd recommend you
use when you make your own games.  You'll see `while True` loops in a lot of games
but it's pretty simple to convert to recursive instead!  You just need an equivalent to 
screen.ontimer that will call your main game function on a schedule.