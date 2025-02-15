from turtle import Turtle, Screen
import random
import turtle

tommy = Turtle()
tommy.shape("turtle")
turtle.colormode(255)

colors = ["yellow", "green", "red", "blue", "orange", "purple"]





length = 0
for i in range(200):
    for j in range(6):
        tommy.pencolor(colors[j])
        # tommy.pencolor(colors[x%6]) # Lze použít i takto a nemusí tu být druhý for cyklus
        tommy.forward(length)
        tommy.left(60)
        length += 1










my_screen = Screen()
my_screen.exitonclick()