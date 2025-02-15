from turtle import Turtle, Screen

arrow = Turtle("arrow")
arrow.pencolor("red")
arrow.pen(fillcolor="blue")
arrow.begin_fill()

for _ in range(4):
    arrow.forward(80)
    arrow.left(90)
arrow.end_fill()




screen = Screen()
screen.exitonclick()