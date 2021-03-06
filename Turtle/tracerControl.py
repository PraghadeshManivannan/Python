# turtle. tracer(n=None, delay=None)
# Parameters: n – nonnegative integer
# delay – nonnegative integer
# Turn turtle animation on/off and set delay for update drawings. 
# If n is given, only each n-th regular screen update is really performed. 
# (Can be used to accelerate the drawing of complex graphics.) 
# When called without arguments, returns the currently stored value of n.
# Second argument sets delay value (see delay()).

import turtle
turtle = turtle.Turtle()

screen = turtle.getscreen()

screen.tracer(8, 25)
dist = 2
for i in range(200):
    turtle.fd(dist)
    turtle.rt(90)
    dist += 2
