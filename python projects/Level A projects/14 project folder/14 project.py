
#!: Make the Higher lower game 
# Todo: Use available dictionary (contestants.py) and art (ascii_art.py).
# Todo: Generate a random accout from the dictionary.
# Todo: Format the account data into printable format.
# Todo: Ask player for a guess.
# Todo: Check if player is correct.
# Todo: provide feedback to player (ie. round counter, whether they guessed right or not).
# Todo: If player is correct have Celeb in B position move to celeb A position.
#* Solution starts on line 100

























































































# from ascii_art import logo, vs                      # Kept imports on same line
# from contestants import data
# import random

# def format(account):                                # Simplified picking Celebs from list
#     account_name = account["name"]
#     account_descr = account["description"]
#     account_coun = account["country"]
#     return f"{account_name}, a {account_descr}, from {account_coun}"

# def compare(guess, a_follow, b_follow):             # Simplifies comparing of followers and also the guess choice
#     if a_follow > b_follow:
#         return guess == "a"
#     else:
#         return guess == "b"
         
# score = 1
# game = True
# account_b = random.choice(data)
# print("".join(logo))                                # Intital print statement when game starts

# while game:
#     account_a = account_b
#     account_b = random.choice(data)
#     if account_a == account_b:
#         account_b = random.choice(data)

#     print(f"Compare A: {format(account_a)}.")       # Prints who the 2 Celebs to compare are
#     print("".join(vs))
#     print(f"Compare B: {format(account_b)}.")
#     guess = input("Who has more followers? Type 'A' or 'B'").lower()

#     print("\n" * 30)
#     print("".join(logo))                            # Prints Top logo every new round

#     a_follow = account_a["follower_count"]          # Identifies how many followers each celeb has
#     b_follow = account_b["follower_count"]

#     correct = compare(guess, a_follow, b_follow)    # Stores the compare function 

#     if correct:                                     # Correct answer process
#         score += 1
#         print(f"you got it! onto round {score}")

#     else:                                           # Wrong answer process
#         print(f"That's wrong, you only made it to round {score}")
#         game = False