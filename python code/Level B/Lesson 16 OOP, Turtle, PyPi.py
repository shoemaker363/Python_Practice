
#! OOP
#$ OOP (Object Oriented Programming)
##  Organizes software design around data, or Objects rather than Functions and Logic.
##  The core of OOP is Classes and Functions.
##  4 Fundamental Principles: Encapsulation, Inheritance, Abstraction, and Polymorphism.
##  Advantages: Code reusability, Scalability, Efficiency, and easier Collaborations.
#$ Encapsulation
##  Hides Object's internal state and only allows access through a public interface.
##  Helps maintain data integrity, and simplifies code maintenance.
#$ Inheritance
##  Allows a Class to inherit attributes and methods from another Class.
##  Promotes code reuse and hierachical relationships.
#$ Abstraction
##  Models only the relevant attributes and behaviors of entities to create a simplified representation of the system.
#$ Polymorphism
##  Enables methods to be implemented differently across various Classes.
##  Allows Objects of different types to be treated as common types.
#$ Class
##  Blueprint or template used to create Objects and defines their stucture and behavior.
#$ Object
##  Fundamental unit that combines Data and the Functions that operate on that data.
#$ Imperative Programming
##  The use of statements on software that change a processes state.
##  Describes how a program operates step by step.
#$ Procedural Progamming
##  Classified as Imperative Programming.
##  Implements behavior of a computer program as procedures (i.e. Functions) that call each other.

#! Turtle
#* Detailed overview of turtle commands and colors.
#@  Turtle Graphics: https://docs.python.org/3/library/turtle.html
#@  Turtle Colors: https://cs111.wellesley.edu/reference/colors

#*  Brief overview of turtle commands with VScode.
import turtle               #? Imports the module 'turtle'.

screen = turtle.Screen()    #? Initialize a screen for turtle.
t = turtle.Turtle()         #? Defines the Class 'Turtle' to 't'. The 't' variable becomes an Object.

t.color("seagreen3")        #? Changes color of line drawn with turtle.
t.forward(100)              ## Tells the turtle how to move. 
t.left(120)
t.forward(100)
t.left(120)                 ## Turns turtle left.
t.forward(100)              ## Moves turtle forward.

t.up()                      ## Picks up turtle, turtle does not draw in Up position.
t.right(60)
t.forward(50)
t.down()                    ## Puts down turtle, turtle can draw in this position.

t.shape("turtle")           ## Changes the look of the turtle on Turtle Graphics

t.color("red4")
t.fillcolor("deepskyblue")  #To Starting point for tracking shape that you want filled and with what color.
t.begin_fill()
t.backward(100)             ## Moves turtle backwards.
t.right(120)                ## Turns turtle right.
t.backward(100)
t.right(120)
t.backward(100)
t.end_fill()                #To End point for shape you want filled. Adds the color at this point.

t.home()                    #? The turtle moves to home position.

print(t)                    ## Prints the string representation of turtle Object, normally includes type and memory address.
print(screen.canvheight)    ## Prints current height of the drawing canvas.
print(screen.canvwidth)     ## Prints current width of the drawing canvas.

turtle.exitonclick()        #? Keeps the turtle screen open after program finishes.



#! Python Packages and PyPi
#$ Useful links for more information.
#@  Python Package Index: https://pypi.org/
#@  Prettytable: https://pypi.org/project/prettytable/
#To  Install command for VScode: pip install PrettyTable.
#@  Google Code Archives: https://code.google.com/archive/p/prettytable/wikis/Tutorial.wiki

from prettytable import PrettyTable, TableStyle         #? Imports PrettyTable and TableStyle.
p = PrettyTable()                                       #? Defines the Class 'PrettyTable' and makes it variable 'p'. 


                                                        ## The 3 lines below make columns with entries for ascii table.
p.add_column("Pokemon Name", ["Terapagos", "Pangoro", "Aromatisse", "Wailord", "Crustle", "Steelix", "Ampharos", "Goomy", "Hoopa", "Jumpluff", "Swalot", "Slugma"])
p.add_column("Type", ["Stellar + Normal", "Fighting + Dark", "Fairy", "Water", "Bug + Rock", "Steel", "Electric", "Dragon", "Phychic + Ghost", "Grass + Flying", "Poison", "Fire" ])
p.add_column("ID", ["1024B", "092", "130", "028", "024", "054", "129", "019", "152", "137", "099", "153"])
p.align = "r"                                           #? Sets alignment of entries to the right. Options: 'l', 'c', and 'r'.
p.set_style(TableStyle.DOUBLE_BORDER)                   #? Changes border style of the table. 'DOUBLE_BORDER' is the variable to change.
print(p)                                                ## Print the ascii table.