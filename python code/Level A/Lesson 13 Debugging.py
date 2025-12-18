
#! Debugging    (This is a good skill to work on to help with coding)

#? This tag: States the Line and what it is
#* This tag: Is line Formatted right and does it have the right amount of Indentation required.
#@ This tag: Describes what the line says it would do.
## This tag: Details.
#$ This tag: Says what the problem is.
#To: This tag: labels the Lines for easy identification
# Todo: This tag: States the fix with the fix coding below it. 


#! Tips
#? Take a Break:
#@    If you have been stuck awhile, Step away and do something else. ("Don't burn yourself out trying to fix a problem.")

#? Ask a Friend:
#@    When you are stuck, there is no shame in having a friend look over your code for the problem.

#? Run Often:
#@    Run the program as much as possible to fix bugs when they do appear

#? Look through StackOverflow
#@    You can look through the already posted problems to see if any of the solutions can help you.



#! Describing the function and the problem.
# def my_function():                      #To Line 1
#     for i in range(1, 20):              #To Line 2
#         if i == 20:                     #To Line 3
#             print("You got it!")        #To Line 4
# my_function()                           #To Line 5

#?      Line 1: Function
#*      Proper Indentation.
#*      Proper Format.
#@      Makes a function with def, the following word is the functions Name/ID "my_function".

#?      Line 2: "For" loop
#*      Proper Format.
#*      Proper Indentation following the function.
#@      The for loop is that "i" has a range of 1 through 20.
##      Range will have integers 1, 2, 3, 4, 5, 6, 7, 8 , 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19. 

#?      Line 3: "If" statement 
#*      Proper Indentation off the "for" loop.
#*      Proper Format.
#@      The if statement is selecting a single number from the range in the for loop to have something happen.
#$      This will not happen as there is no integer of 20 in "i" with the range of 1-20.

#?      Line 4: Print statement
#*      Proper Indentation off the "if" statement.
#*      Proper Format.
#@      The print statement prints "You got it!" only when "i" equals 20.
#$      Will not print due to the "if" statement not being able to get the number 20.

#?      Line 5: Calling the Function
#*      Proper Indentation.
#*      Proper Format.
#@      Calls the defined function so it can start its process.

# Todo The fix is to increase range to 21 so the that 20 gets added into the range.
# def my_function():
#     for i in range(1, 21):
#         if i == 20:
#             print("You fixed it")
# my_function()


#! Reproducing a Bug

# from random import randint                                      #To Line 1
# dice_images = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣"]           #To Line 2
# dice_num = randint(1, 6)                                        #To Line 3
# print(dice_images[dice_num])                                    #To Line 4

#?      Line 1: Importing
#*      Proper Indentation.
#*      Proper Format.
#@      Accesses "random" module and imports the specific variable that will be used.

#?      Line 2: Variable
#*      Proper Indentation.
#*      Proper Format.
#@      This makes the variable "dice_images" equal to the list "[]" and any time the 
#@      variable is called the list is what is being sent.
##      List contains the images 1, 2, 3, 4, 5, 6.
#$      The first image in the list is in the 0 position.

#?      Line 3: Variable
#*      Proper Indentation.
#*      Proper Format.
#@      This makes the variable "dice_num" equal to a random integer and any time the
#@      variable is called upon, a single integer is selected to represent the variable.
##      randint will pick and then provide a single interger in the range of 1 to 6.
##      Available integers in randint 1 to 6 are  1, 2, 3, 4, 5, 6.
#$      Can not select the first image available due to not having the integer of 0 and the 
#$      integer 6 is trying to select an image that does not exist in the list 

#?      Line 4: Print Statement
#*      Proper Indentation.
#*      Proper Format.
#@      Prints a image from the "dice_image" list that is picked by the "dice_num" randint choice.
##      Print is putting a image in terminal from list of choices in "dice_image" variable.
##      The image that gets printed is being decided by the integer provided by "dice_num" variable.

# Todo  The fix is to change the integers available to randint to 0, 5
# from random import randint                             
# dice_images = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣"]           
# dice_num = randint(0, 5)                                        
# print(dice_images[dice_num])  


#! Practice

# year = int(input("Whats your year of birth? "))     #To Line 1

# if year > 1980 and year < 1994:                     #To Line 2
#     print("You are a millenial")                    #To Line 3
# elif year > 1994:                                   #To Line 4
#     print("You are a Gen Z. AKA just a baby!")                       #To Line 5

#?      Line 1: Variable from an input
#*      Proper Indentation.
#*      Proper Format.
#@      The variable "year" is equal to the input from the user, and made into an integer from the 
#@      int class attached to the input. Input is asking for user to enter a string to use with program.
##      int class: Takes a number or string and converts it to an integer.
##      input function: Shows user a printed statement that needs a reply. The reply is stored as a string. 

#?      Line 2: If statement
#*      Proper Indentation.
#*      Proper Format.
#@      The "if statement" asks if the following variables are present or have happened.
##      "year > 1980": if "year" variable is greater than 1980.
##      "and": to include with the first part.
##      "year < 1994": if "year" variable is less than 1994.
#$      Does not include the year of 1994, Stops at 1993

#?      Line 3: Print Statement
#*      Proper Indentation to recieve from "if statement".
#*      Proper format.
#@      Prints the string inside the parentheses.

#?      Line 4: Elif statement
#*      Proper Indentation to start if the "if statement" didn't run.
#*      Proper Format.
#@      The "elif statement" asks if the following variables are present or have happened.
#@      An "elif statement" can only happen if the "if statement" did not run.
##      "year > 1994": if "year" variable is greater than 1994.
#$      Does not include the year of 1994, Starts counting from 1995

#?      Line 5: Print Statement
#*      Proper Indentation to receive from "elif statement".
#*      Proper format.
#@      Prints the string inside the parentheses.

# Todo  The fix is to add an "=" to the "if statement" (year < 1994) or 
# Todo  to the "elif statement" (year > 1994). Depends on what your code is doing.
# year = int(input("Whats your year of birth? "))     

# if year > 1980 and year <= 1994:                     
#     print("You are a millenial")                    
# elif year > 1994:                                   
#     print("You are a Gen Z. AKA just a baby!")  



#! Error fixing (multiple steps)

#? Step 1: Initial program
#! The problem with this program lies in what the user types for the input.
#! The program can not run an a string that is not numerically typed.
# age = int(input("How old do you think Dom is? "))

# if age > 29:
#     print("Dom is not older than dirt!!!! 🤣")
# elif age <= 29 and age > 25:
#     print("That seems about right for Dom!")
# else:
#     print("You must think Dom is a baby?!?!?! 🐣")

#! run program and when responding to the input, type a numbers word with letters. (i.e. thirty )
#? Step 2: The terminal should give an error like this in response:
##             age = int(input("How old do you think Dom is? "))
##             ValueError: invalid literal for int() with base 10: 'twelve'

# Todo The fix for user error, put in a "try statement" and print a more detailed input option
# try:
#     age = int(input("How old do you think Dom is? "))
# except ValueError:                                    ## ValueError was retrieved from the terminal after error occured.
#     print("You have typed in an invalid number. Please try again with a numerical number.")
#     age = int(input("How old do you think Dom is? "))
#                                     #@ This fix is just giving the user another chance to correctly format there input.
# if age > 29:
#     print("Dom is not older than dirt!!!! 🤣")
# elif age <= 29 and age > 25:
#     print("That seems about right for Dom!")
# else:
#     print("You must think Dom is a baby?!?!?! 🐣")



#! Using Print statement to fix issues
#? Step 1: Initial program
# white_monster = 0
# non_white_monster = int(input("How many drinks have you had that were not White Monsters today? Please enter a numerical number: "))
# white_monster == int(input("How many White Monsters (Best hydration source) have you had today? Please enter a numerical number: "))
# amount = white_monster / non_white_monster

# print(amount)


#? Step 2: add some print statements
# white_monster = 0
# non_white_monster = int(input("How many drinks have you had that were not White Monsters today? Please enter a numerical number: "))
# white_monster == int(input("How many White Monsters (Best hydration source) have you had today? Please enter a numerical number: "))
# amount = white_monster / non_white_monster

# print(f"bad drinks = {non_white_monster}")
# print(f"Best drink = {white_monster}")
# print(amount)
#@ Find out the problem from the prin statements.

#? Step 3: Fix the problem
# white_monster = 0
# non_white_monster = int(input("How many drinks have you had that were not White Monsters today? Please enter a numerical number: "))
# white_monster = int(input("How many White Monsters (Best hydration source) have you had today? Please enter a numerical number: "))
# amount = white_monster / non_white_monster

# print(f"bad drinks = {non_white_monster}")
# print(f"Best drink = {white_monster}")
# print(f"Mr.Dom TutePro has only had {amount} White Monsters today.\n This is not enough, bring the funnel!!!")