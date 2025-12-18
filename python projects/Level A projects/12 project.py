
#! Making a number guessing game.
# Todo Range of numbers will be from 1 to 100.
# Todo Have 2 difficulty modes in the same program: Easy and Hard.
# Todo Easy Mode: User will have 10 attempts to guess the number.
# Todo Hard Mode: User will have 5 attempts to guess the number.
#* Solution starts on line 100




























































































# from random import randint

# EASY_MODE = 10
# HARD_MODE = 5


# def check(player, actual, turns):
#     if player > actual:
#         print("You guessed to high")
#         return turns - 1
#     elif player < actual:
#         print("You guessed to low.")
#         return turns - 1
#     else:
#         print(f"Winner, you have guessed the correct number of {actual}")


# def difficulty():
#     level = input("Would you like to play on 'hard' or 'easy' mode? ").lower()        
#     if level == "easy":
#         return EASY_MODE
#     elif level == "hard":
#         return HARD_MODE
        
                
# def game(): 
#     print("Welcome to a guessing a number game!")
#     number = randint(1, 100)

#     turns = difficulty()
    
#     guess = 0
#     while guess != number:
#         print(f"You have {turns} attempts remaining")
#         guess = int(input("What is your guess? "))
        
#         turns = check(guess, number, turns)
#         if turns == 0:
#             print("You are out of guesses. You lose!")
#             return
#         elif guess != number:
#             print("guess again: ")
# while input("Do you want to play again? 'yes' or 'no': ").lower() == "yes":
#     print("\n" * 30)
#     game()