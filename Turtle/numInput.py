import turtle
turtle = turtle.Turtle()

screen = turtle.getscreen()

# turtle. numinput(title, prompt, default=None, minval=None, maxval=None)
# Parameters: title – string
# prompt – string
# default – number (optional)
# minval – number (optional)
# maxval – number (optional)
# Pop up a dialog window for input of a number.
# title is the title of the dialog window, prompt # is a text mostly describing what numerical information to input. 
# default: default value,minval: minimum value for imput, maxval: maximum value for input.
# The number input must be in the range minval .. maxval if these are given. 
# If not, a hint is issued and the dialog remains open for correction. Return the number input. 
# If the dialog is canceled,return None.

num = screen.numinput('Lucky Number','Enter your lucky number :',1,minval=0,maxval=10)
print(num)