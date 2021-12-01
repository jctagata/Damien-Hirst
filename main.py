import turtle as t
import random as r

color_list = [(131, 166, 205), (222, 148, 106), (31, 42, 61), (199, 134, 147), (165, 59, 48),
              (140, 184, 162), (39, 105, 157), (238, 212, 89), (152, 58, 66), (217, 81, 70),
              (169, 29, 33), (236, 165, 156), (50, 112, 90), (35, 61, 55), (17, 97, 71), (156, 33, 30),
              (231, 160, 165), (53, 44, 49), (170, 188, 221), (57, 51, 48), (189, 100, 110), (31, 60, 109),
              (103, 127, 161), (34, 151, 209), (174, 200, 188), (65, 66, 56)]

t.colormode(255)
timmy = t.Turtle()
timmy.speed("fastest")
timmy.penup()
timmy.hideturtle()
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)
number_of_dots = 100

for dot in range(1, number_of_dots + 1):
    timmy.dot(20, r.choice(color_list))
    timmy.forward(50)

    if dot % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)

screen = t.Screen()
screen.exitonclick()





