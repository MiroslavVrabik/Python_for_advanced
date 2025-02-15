# Turtle graphics
from turtle import Turtle, Screen

tommy = Turtle()
tommy.shape("turtle")
tommy.color("red", "green")
tommy.forward(50)
tommy.right(45)
tommy.backward(40)


my_screen = Screen()
my_screen.bgcolor("black")
my_screen.exitonclick()