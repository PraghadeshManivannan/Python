import turtle

turtle = turtle.Turtle()

#turtle. undo()
#Undo (repeatedly) the last turtle action(s).
# Number of available undo actions is determined by the size of the undobuffer

for i in range(9):
    turtle.fd(50)
    turtle.lt(80)

for i in range(18):
    turtle.undo()
