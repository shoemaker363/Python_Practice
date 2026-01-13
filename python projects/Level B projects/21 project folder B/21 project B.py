
#!      Make a United States guessing game for each state name.

# TODO: Have users guess be 'Title' cased.
# TODO: Check to see if users guess is one of the 50 states.
# TODO: Have correct guesses appear on map.
# TODO: Allow users to keep playing until they get stuck or finish.
# TODO: Have a file created with all the states the user is unable to guess.

#* Solution starts on line 100.

























































































# import turtle
# import pandas

# screen = turtle.Screen()
# screen.title("State Name Game")                                                     ## Turtle screen title.
# image = "python projects/Level B projects/21 project folder B/united_states.gif"    ## Makes image accessible.
# screen.addshape(image)                                                              ## Makes image into Turtle shape.
# turtle.shape(image)                                                                 ## Produces shape on Turtle screen.

# t = turtle.Turtle()
# t.hideturtle()
# t.penup()

# # #$ Finding x, y coordinates on turtle screen.
# # def get_mouse_click_coor(x, y):                     
# #     print(x, y)                                     ## Takes user's click on Turtle screen and prints the x, y coordinates.
# # turtle.onscreenclick(get_mouse_click_coor)          ## Registers where user clicks on Turtle screen.
# # turtle.mainloop()                                   ## Keeps Turtle screen open. 

# data_on_states = pandas.read_csv("python projects/Level B projects/21 project folder B/states.csv")
# data = data_on_states["state"].to_list()
# user_guess = []

# while len(user_guess) < 50:
#     user_state_guess = screen.textinput(title=f"{len(user_guess)} States Guessed!", prompt="Guess a State name:").title()

#     if user_state_guess == "Exit":
#         missing_states = []
#         for state in data:
#             if state not in user_guess:
#                 missing_states.append(state)
#         new_data = pandas.DataFrame(missing_states)
#         new_data.to_csv("python projects/Level B projects/21 project folder B/need_to_learn.csv")
#         break
#     if user_state_guess in data and not user_guess:
#         user_guess.append(user_state_guess)
#         states = data_on_states[data_on_states.state == user_state_guess]
#         t.goto(states.x.item(), states.y.item())
#         t.write(user_state_guess)
#     if user_state_guess in data and user_guess:
#         t.write(user_state_guess)

# screen.exitonclick()