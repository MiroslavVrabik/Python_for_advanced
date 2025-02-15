from turtle import Turtle, Screen

tommy = Turtle()
lemmy = Turtle()


lemmy.pencolor("green")
tommy.pencolor("red")

tommy.circle(10)



for i in range(15, 50, 5):
    lemmy.circle(i)


my_screen = Screen()
my_screen.exitonclick()