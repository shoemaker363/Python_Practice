import turtle
from turtle import Turtle, Screen

#! GUI (Graphical User Interface) and Turtle
#@  turtle Documentation: https://docs.python.org/3/library/turtle.html
#@  trinket colors: https://trinket.io/docs/colors
#@  turtle colors: https://cs111.wellesley.edu/reference/colors

t = Turtle()                          ## (Do not comment out this line) Changes the name of the turtle to new variable name 't'

# t.shape("triangle")                 ## Changes shape of the turtle icon on the screen

# t.color("skyblue")                  ## Changes color of the turtle icon on the screen

# #* turtle movement
# t.fd(150)                           #? ('forward') Moves turtle forward in direction its facing by the amount input.

# t.rt(75)                            #$ ('right') Turns turtle right in the amount of degrees input.

# t.bk(200)                           #? ('backward'/'back') Moves turtle backwards from the direction its facing by the amount input.

# t.lt(100)                           #$ ('left')Turns turtle left in the amount of degrees input.

# t.goto(70, 75)                      #? ('setposition'/'setpos') Turtle moves to coordinates in the input. (If the pen is down, will draw along the way.)

# t.teleport(175, 175)                #$ Turtle moves to coordinates in the input. (Line is not drawn.)

# t.setx(25)                          #? Changes the turtles x coordinate without changing the y coordinate

# t.sety(25)                          #$ Changes the turtles y coordinate without changing the x coordinate.

# t.heading()                         #? Requires integer/float to be below the method line. Sets angle to desired degree
# 90                                  ## ('setheading') Alternate to 'heading' has number inside the paranthesis. Sets angle to desired degree

# t.home()                            #$ Moves turtle back to point of origin.

# t.circle(40, 180)                   #? Makes a circle. First number = radius. Second number = how much of circle drawn. 

# t.dot(40, "red")                    #$ Makes a dot starting at the center of turtle. Number = size of dot. String = color of dot.

# stamp_id = t.stamp()                #? ('stamp()') Makes a stamp of turtle shape onto current canvas position of the turtle.

# t.clearstamp(stamp_id)              #$ Used to delete a specific stamp ID.

# t.undo()                            #? Undo the last action.

# t.speed(5)                          #? How fast the turtle moves. range of: slowest 1 to 10 fast and 0 being the fastest. 


# #! Draw a square with turtle
# t.fd(100)
# t.lt(90)
# t.fd(100)
# t.lt(90)
# t.fd(100)
# t.left(90)
# t.forward(100)
# t.left(90)

# #! Draw a square with a for loop
# for _ in range(4):
#     t.fd(100)
#     t.lt(90)


#! Some advice on imports
#? If only importing a Class to use a couple times in code,
#? then just type the simple version of import Module,
#? and just type the Class you need from the Module.
##  ex.     import turtle 
##          t = turtle.Turtle()

#? If you ever have a really long Module name,
#? you can import Module as Variable.
##  ex.     import turtle_turtle_turtle as z
##          t = z.Turtle()

#? If you need the Class a few times or more in your code,
#? then use the from Module import Class.
##  ex.     from turtle import Turtle
##          t1 = Turtle()
##          t2 = Turtle()
##          t3 = Turtle()

# #! Drawing a dashed line
# for _ in range(8):
#     t.fd(20)
#     t.up()                            ## ('penup'/'pu') Picks pen up so it can not draw.    
#     t.fd(10)
#     t.down()                          ## ('pendown'/'pd') Puts pen down to draw again.

# #! Drawing different shapes.
# import random
# t.speed(2)
# t.teleport(0, 200)

# def color():
#     R = random.random()
#     B = random.random()
#     G = random.random()
#     t.color((R, G, B))

# for _ in range(3):          #* Triangle
#     t.fd(100)
#     t.rt(120)
    
# color()
# for _ in range(4):          #* Square
#     t.fd(100)
#     t.rt(90)

# color()
# for _ in range(5):          #* Pentagon
#     t.fd(100)
#     t.rt(72)

# color()
# for _ in range(6):          #* Hexagon
#     t.fd(100)
#     t.rt(60)

# color()
# for _ in range(7):          #* Heptagon
#     t.fd(100)
#     t.rt(51.43)

# color()
# for _ in range(8):          #* Octagon
#     t.fd(100)
#     t.rt(45)

# color()
# for _ in range(9):          #* Nonagon
#     t.fd(100)
#     t.rt(40)

# color()
# for _ in range(10):         #* Decagon
#     t.fd(100)
#     t.rt(36)

# #! Drawing shapes with function
# import random

# t.speed(2)
# t.teleport(0, 200)

# def color():
#     R = random.random()
#     B = random.random()
#     G = random.random()
#     t.color((R, G, B))

# def draw(sides):
#     angle = 360 / sides
#     for _ in range(sides):
#         t.fd(100)
#         t.rt(angle)
# for shape_side in range(3, 11):
#     color()
#     draw(shape_side)

# screen = Screen()                       ## Names the screen that turtle operates on
# screen.exitonclick()                    ## Keeps the screen open until user clicks on it, Otherwise the screen closes when turtle is done.

# #! Random path for turtle with random color

# #@ Python Tuples: EX. tuple = (1, 5, 8)
# #? Tuples do not support item assignment like lists.

# import random
# turtle.colormode(255)

# def color():
#     R = random.randint(0, 255)
#     G = random.randint(0, 255)
#     B = random.randint(0, 255)
#     t.color((R, G, B))

# def moving():
#     speed = random.randint(0, 11)       ## changes the speed of each line drawn
#     rotate = random.randint(0, 360)     ## changes the direction of each line drawn
#     width = random.randint(1, 30)       ## changes the thickness of  each line drawn
#     t.fd(100)                           ## length of each line is 100 (can be in while statement if wanted.)
#     t.lt(rotate)
#     t.width(width)
#     t.speed(speed)

# for _ in range(200):
#     color()
#     moving()

# screen = Screen()

# #! Drawing a spirograph
# import random
# t.speed(0)
# turtle.colormode(255)

# def color():
#     R = random.randint(0, 255)
#     G = random.randint(0, 255)
#     B = random.randint(0, 255)
#     t.color((R, G, B))

    
# for _ in range(100):
#     t.circle(157)
#     t.left(10)
#     color()

# screen = Screen()
# screen.exitonclick()