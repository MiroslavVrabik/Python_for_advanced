from turtle import Turtle, Screen

tommy = Turtle()
tommy.shape("turtle")

for i in range(4):
    tommy.forward(50)
    tommy.right(90)


my_screen = Screen()
my_screen.exitonclick()