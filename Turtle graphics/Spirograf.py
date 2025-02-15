# importy
from turtle import Turtle, Screen
import random
import turtle

# Změna barevného módu
turtle.colormode(255)


tommy = Turtle()
tommy.shape("turtle")
tommy.speed(20)
tommy.pensize(4)
# colors = ["azure2", "brown4", "chartreuse", "coral1", "cornsilk2", "DarkMagenta", "DarkSeaGreen3", "DeepSkyBlue4"]
# Funkce na generování barvy
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

def spirograf(gap, size):
    for number in range(int(360/gap)):
        tommy.pencolor(random_color())
        tommy.circle(size)
        tommy.left(gap)

spirograf(2, 100)



my_screen = Screen()
my_screen.exitonclick()
