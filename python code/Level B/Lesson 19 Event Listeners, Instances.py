
#! Higher Order of Functions and Event Listners.
#@ Turtle listener documents: https://docs.python.org/3/library/turtle.html#turtle.listen 

# ## Listners are using function as a input.

# from turtle import Turtle, Screen

# t = Turtle()
# screen = Screen()

# def forward_move():
#     t.fd(10)

# screen.listen()
# screen.onkey(key="space", fun=forward_move) ## Do not add parentheses to the 'forward_move' function, doing so causes the fuction to activate without need for key listner.
# screen.exitonclick()

# ## Simpler example of function as a input.
#                                 ## _
# def add(n1, n2):                ##  |
#     return n1 + n2              ##  |           These are Functions being used as inputs.
#                                 ##  |
# def subtract(n1, n2):           ##  |
#     return n1 - n2              ##  |
#                                 ##  |
# def multiply(n1, n2):           ##  |
#     return n1 * n2              ##  |
#                                 ##  |
# def divide(n1, n2):             ##  |
#     return n1 / n2              ## _|

# def calculator(n1, n2, func):
#     return func(n1, n2)

# result = calculator(2, 3, multiply)     ## Changing the fuction name here changes which fuction is being called. 
#                                         #?  'add', 'subtract', 'multiply', 'divide'
# print(result)

# #! etch-a sketch like program

# from turtle import Turtle, Screen
# t = Turtle()
# screen = Screen()

# def forward_move():
#     t.fd(5)

# def backward_move():
#     t.bk(5)

# def left_turn():
#     t.lt(1)

# def right_turn():
#     t.rt(1)

# def clear():
#     screen.reset()
#     screen.setworldcoordinates(0, 0, 0, 0)

# screen.listen()
# screen.onkeypress(key="w", fun=forward_move)
# screen.onkeypress(key="s", fun=backward_move)
# screen.onkey(left_turn, "a")                    ## alternate way of typing out function with key
# screen.onkey(right_turn, "d")
# screen.onkey(key="c", fun=clear)

# screen.exitonclick()

#! Object State and Instances

from turtle import Turtle, Screen
import random

# good_to_race = False

# color = ["red", "orange", "yellow", "blue", "black", "purple", "green"]
# position = [-181, 12, 74, 134, -115, 190, -52]
# shape = ["arrow", "turtle", "square", "classic", "arrow", "triangle", "circle"]
# turtle_list = []

# print(color)
# screen = Screen()
# screen.setup(width=500, height=400)             ## 'Width' and 'Height' words with equal sign are not needed, but it does make reading the code easier for anyone reading the code.
# race_bet = screen.textinput(title="Turtle racing", prompt="What color turle will win the race?")
# print(f"Interesting choice going with {race_bet} Dom.")



# for t_index in range(0, 7):
#     new_t = Turtle(shape=shape[t_index])
#     new_t.color(color[t_index])
#     new_t.penup()
#     new_t.goto(-235, y=position[t_index])
#     turtle_list.append(new_t)

# if race_bet:
#     good_to_race = True

# while good_to_race:

#     for turtle in turtle_list:
#         if turtle.xcor() > 230:
#             good_to_race = False
#             winner = turtle.pencolor
            
#             if winner == race_bet:
#                 print("Nice pick Dom! Here is a cookie")
#             else:
#                 print("Go find some luck luck Dom!")


#         rando_distance = random.randint(0, 10)
#         turtle.fd(rando_distance)

# screen.exitonclick()