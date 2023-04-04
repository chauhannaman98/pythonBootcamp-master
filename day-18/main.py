from turtle import Turtle, Screen
from random import randint, choice
import secrets

tim = Turtle()
directions = ["forward", "backward", "right", "left"]
travel_distance = 20

screen = Screen()
screen.colormode(255)
tim.width(4)
tim.speed(10)

for _ in range(1000):
    r: int = randint(0, 256)
    g: int = randint(0, 256)
    b: int = randint(0, 256)
    tim.pencolor(r, g, b)
    random_index = randint(0, 3)
    selected_direction = directions[random_index]
    if selected_direction == 'forward':
        tim.forward(travel_distance)
    elif selected_direction == 'backward':
        tim.backward(travel_distance)
    elif selected_direction == 'right':
        tim.right(90)
        tim.forward(travel_distance)
    elif selected_direction == 'left':
        tim.left(90)
        tim.forward(travel_distance)

screen.exitonclick()
