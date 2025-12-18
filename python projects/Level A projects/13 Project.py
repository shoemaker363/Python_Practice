
# Todo: Run through each of the codes and see if you can debug them.
#*      Solutions start on line 100

#! Code 1
# def odd_or_even(number):
#     if number % 2 = 0:
#         return "This is an even number."
#     else:
#         return "This is an odd number."
    


#! Code 2
# def is_leap(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 4000 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False



#! Code 3
# def fizz_buzz(target):
#     for number in range(1, target + 1):
#         if number % 3 == 0 or number % 5 == 0:
#             print("FizzBuzz")
#         if number % 3 == 0:
#             print("Fizz")
#         if number % 5 == 0:
#             print("Buzz")
#         else:
#             print([number])




























































#? Code 1 Solution
# def odd_or_even(number):
#     if number % 2 == 0:         # Add an "="
#         print("This is even.")  # Not required, Just here for visual verification                
#         return "This is an even number."
#     else:
#         print("This is odd.")   # Not required, Just here for visual verification 
#         return "This is an odd number."


# odd_or_even(2024)               # put a call function in place to run


#? Code 2 Solution
# def is_leap(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:     # Need to delete an extra 0, 4000 should be 400
#                 print("True")       # Not required, Just here for visual verification
#                 return True
#             else:
#                 print("False")      # Not required, Just here for visual verification
#                 return False
#         else:
#             print("true")       # Not required, Just here for visual verification
#             return True
#     else:
#         print("false")      # Not required, Just here for visual verification
#         return False
    
# is_leap(396)        # put a call function in place to run


#? Code 3 Solution
# def fizz_buzz(target):
#     for number in range(1, target + 1):
#         if number % 3 == 0 and number % 5 == 0:     # Change "or" into "and"
#             print("FizzBuzz")
#         elif number % 3 == 0:       # Change "if" into "elif"
#             print("Fizz")
#         elif number % 5 == 0:       # Change "if" into "elif"
#             print("Buzz")
#         else:
#             print(number)       # Removed "[]"

# fizz_buzz(30)       # put a call function in place to run