from turtle import Turtle, Screen
import random


# for i in range(20):
#     first_color = random.randint(0, 255)
#     print(first_color)
tommy = Turtle()
tommy.shape("turtle")
pepa = Turtle()
moves_pepa = 3
tommy_length = 50
pepa_length = 100
degrees = 360

colors = ["azure2", "brown4", "chartreuse", "coral1", "cornsilk2", "DarkMagenta", "DarkSeaGreen3", "DeepSkyBlue4"]

for i in range(3,10):
    random_color = random.choice(colors)
    tommy.pencolor(random_color)
    for _ in range(i):
        tommy.forward(tommy_length)
        tommy.right(degrees/i)

while moves_pepa != 9:
    random_color = random.choice(colors)
    pepa.pencolor(random_color)
    for _ in range(moves_pepa):
        pepa.forward(pepa_length)
        pepa.right(degrees/moves_pepa)
    moves_pepa += 1


my_screen = Screen()
my_screen.exitonclick()
