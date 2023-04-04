from turtle import Turtle, Screen
from random import randrange

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet",
                            prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue"]
turtles = []
turtles_distance = [0, 0, 0, 0, 0]

if user_bet in colors:
    for i in range(0, 5):
        new_turtle = Turtle(shape="turtle")
        new_turtle.penup()
        new_turtle.goto(x=-230, y=100 - (50 * i))
        new_turtle.color(colors[i])
        turtles.append(new_turtle)
    is_race_on = True
    while is_race_on:
        for i in range(0, 5):
            distance = randrange(0, 10)
            turtles[i].forward(distance)
            turtles_distance[i] += distance
            if turtles_distance[i] >= 440:
                is_race_on = False
                turtles[i].write(f"{colors[i]} won!", align="center")
                if colors[i] == user_bet:
                    print(f"You've won the bet! The winning color is {colors[i]}.")
                else:
                    print(f"You've lost the bet! The winning color is {colors[i]}.")


screen.exitonclick()
