
#! Debugging


#! Describing the function and the problem.
def my_function():                      #To Line 1
    for i in range(1, 20):              #To Line 2
        if i == 20:                     #To Line 3
            print("You got it!")        #To Line 4

#? Line 1: Is making "my_function" into a function.
#*      Proper indentation
#*      Proper format

#? Line 2: The start of the "for" loop.
#*      Proper format
#*      Proper indentation following the function
#@      The for loop is that "i" has a range of 1 through 20.

#? Line 3: Making of an "if" statement for the "for" loop.
#*      Proper indentation off the "for" loop
#*      Proper format
#@      The if statement is selecting a single number from the range in the for loop to have something happen.
#!      This will not happen as there is nothing seperating the differrent integers for "i" and the range of 1-20.

#? Line 4: Print statement.
#*      Proper indentation off the "if" statement
#*      Proper format
#@      The print statement prints "You got it!" only when "i" equals 20.
#!      Will not print due to the "if" statement not being able to only get the number 20. 

##