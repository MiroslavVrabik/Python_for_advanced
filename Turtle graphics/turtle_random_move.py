from turtle import Turtle, Screen
import random
import turtle

# Změna barevného módu
turtle.colormode(255)

tommy = Turtle()
tommy.shape("turtle")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colors = (r, g, b)
    return random_colors


# colors = ["azure2", "brown4", "chartreuse", "coral1", "cornsilk2", "DarkMagenta", "DarkSeaGreen3", "DeepSkyBlue4"]
rotation = [90, 180, 270, 360]
for number in range(200):
    # Náhodný výběr barvy
    tommy.pencolor(random_color())

    # Tloušťka čáry se zvyšuje
    if number <= 10:
        tommy.pensize(number)

    # Náhodný výběr čísel
    random_rotation = random.choice(rotation)

    # Pohyb
    tommy.forward(30)
    tommy.right(random_rotation)

    # Zvšujeme rychlost
    tommy.speed(number)


my_screen = Screen()
my_screen.exitonclick()