# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpeg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

import turtle
import random

turtle.colormode(255)
tim = turtle.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(207, 160, 111), (34, 105, 140), (188, 168, 19), (172, 82, 30), (143, 174, 194), (13, 51, 83), (217, 209, 122), (157, 23, 13), (194, 143, 157), (144, 69, 101), (95, 160, 81), (136, 176, 148), (18, 130, 75), (235, 205, 5), (48, 55, 91), (216, 172, 181), (48, 155, 186), (127, 36, 43), (97, 36, 15), (71, 21, 37), (180, 90, 118), (5, 101, 56), (2, 84, 111), (68, 79, 20), (225, 173, 171), (187, 79, 73)]

tim.setheading(225)
tim.forward(250)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle.Screen()
screen.exitonclick()
