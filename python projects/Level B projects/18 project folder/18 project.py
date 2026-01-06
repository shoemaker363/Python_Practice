import colorgram
import turtle
from turtle import Screen
import random
t = turtle.Turtle()
turtle.colormode(255)
# Todo: Use website url to see how to use colorgram.
#@      https://pypi.org/project/colorgram.py/
# Todo: Extract the colors from the image 'spot.jpg'.

rgb = []
colors = colorgram.extract("python projects/Level B projects/18 project folder/spot.jpg", 20)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new = (r, g, b)
    rgb.append(new)

print(rgb)

# Todo: Make the extracted RGB colors useable with the turtle.
# Todo: Make your own 'spot' image with 100 dots in a 10x10 with randomized coloring from the extracted colors.
#* A solution starts on line 100 
#? There are different types ways to come up with a solution.









































































# list_color = [(148, 7, 23), (211, 159, 20), (203, 72, 7), (206, 151, 141), (234, 204, 2), (124, 1, 7), (228, 207, 83), (202, 150, 155), (178, 23, 1), (170, 172, 178), (150, 56, 76), (220, 175, 184), (170, 102, 116), (221, 178, 171), (183, 102, 88), (187, 189, 200)]

# t.penup()
# t.setpos(-255, 255)
# def move():
#     for _ in range(10):
#         t.dot(20, random.choice(list_color))
#         t.fd(50)

# for _ in range(5):
#     move()
#     t.rt(90)
#     t.fd(50)
#     t.rt(90)
#     t.fd(50)
#     move()
#     t.lt(90)
#     t.fd(50)
#     t.lt(90)
#     t.fd(50)



# screen = Screen()
# screen.exitonclick()