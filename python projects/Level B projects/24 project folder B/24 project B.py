import random
import pandas as pd
from tkinter import *

#!      Create a Flashcard Application

#@          Pandas DataFrame Documentation: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_dict.html

# TODO: Access 'Japanese.csv' file to use for flashcards.
# TODO: Create a window using 'front_of_card.png', 'back_of_card.png', 'right_button.png', and 'wrong_button.png'.
# TODO: Have an automatic way of flipping the flashcard over.
# TODO: Front of flashcard should Japanese word and the Romanization of the Japanese word.
# TODO: Back of flashcard should have English translation of the Japanese word.
# TODO: Have 'right_button' and wrong_button' be the images for 2 seperate buttons.
# TODO: Have 'right_button' represent the user knowing the current flashcard, and removing it from the unknown list.
# TODO: Create a new CSV file to pull all Japanese.csv data over and have new CSV file be where data is deleted with a function.
 
#* Solution starts on line 100.

















































































# current_card = {}
# study = {}

# #$ Reading CSV file:
# try:
#     known_data = pd.read_csv("python projects/Level B projects/24 project folder/project files/unknown_flashcards.csv")
    
# #// Read file: 
# except FileNotFoundError:
#     data = pd.read_csv("python projects/Level B projects/24 project folder B/project files/Japanese.csv")
#     study = data.to_dict(orient="records")                          ## 'orient': Restructures how data is presented.
#                                                                     ## 'records': list like presentation, ex. [{'Japanese': 'テレビ', 'Romanization': 'Terebi', 'English': 'TV'}.

# else:
#     study = known_data.to_dict(orient="records")

# #$ Frontside Flashcard Function:
# def next_card():
#     global current_card, timer

# #// Delete Timer:
#     window.after_cancel(timer)

# #// Visible Text:
#     current_card = random.choice(study)    
#     canvas.itemconfig(title_japan, text="Japanese")
#     canvas.itemconfig(japan, text=current_card["Japanese"], fill="blue")
#     canvas.itemconfig(title_roman, text="Romanization")
#     canvas.itemconfig(roman, text=current_card["Romanization"], fill="blue")
#     canvas.itemconfig(equal, text="🟰")
#     canvas.itemconfig(background_image, image=card_front)

# #// Invisible text:
#     canvas.itemconfig(title_en, text="")
#     canvas.itemconfig(en, text="")

# #// Restart Timer:
#     timer = window.after(3000, func=flip_card)

# #$ Backside Flashcard Function:
# def flip_card():

# #// Visible Text:
#     canvas.itemconfig(title_en, text="English", fill="red")
#     canvas.itemconfig(en, text=current_card["English"], fill="gold")
#     canvas.itemconfig(background_image, image=card_back)

# #// Invisble text:    
#     canvas.itemconfig(title_japan, text="")
#     canvas.itemconfig(japan, text="")
#     canvas.itemconfig(title_roman, text="")
#     canvas.itemconfig(roman, text="")
#     canvas.itemconfig(equal, text="")

# #$ Known flashcard function:
# def known():

# #// If the user clicks correct button/checkmark, removes that flashcard from the dictionary:
#     study.remove(current_card)

# #// Creation of 'unknown_flashcards.csv' with entire 'Japanese.csv':
# #// 'unknown_flashcards.csv' is the file that will have the 'current_card' removed from:
#     data = pd.DataFrame(study)
#     data.to_csv("python projects/Level B projects/24 project folder B/project files/unknown_flashcards.csv", index=False)

#     next_card()

# #$ Window UI:
# window = Tk()
# window.title("Japanese Flash Cards")
# window.config(padx=50, pady=50, bg="dark slate gray")

# #$ Canvas UI:
# canvas = Canvas(width=800, height=526, bg="dark slate gray", highlightthickness=0)
# canvas.grid(column=0, row=0, columnspan=2)
# canvas.config()

# #// Timer:
# timer = window.after(3000, func=flip_card)

# #$ Front Flashcard:
# card_front = PhotoImage(file="python projects/Level B projects/24 project folder B/project files/front_of_card.png")
# background_image = canvas.create_image(400, 263, image=card_front)

# #// Front Flashcard Japanese:
# title_japan = canvas.create_text(150, 150, text="Japanese", font=("Times new Roman", 40, "italic underline"))
# japan = canvas.create_text(150, 300, text="Japanese", font=("Ariel", 40, ""))

# #// Front Flashcard Romanization of Japanese:
# title_roman = canvas.create_text(600, 150, text="Romanization", font=("Times New Roman", 40, "italic underline"))
# roman = canvas.create_text(600, 300, text="Romanization", font=("ariel", 40, ""))

# #// Front Flashcard Equal Sign:
# equal = canvas.create_text(350, 150, text="🟰", font=("", 40, ""))

# #$ Back Flashcard:
# card_back = PhotoImage(file="python projects/Level B projects/24 project folder B/project files/back_of_card.png")

# #// Back Flashcard English Translation:
# title_en = canvas.create_text(400, 150, text="", font=("Times New Roman", 40, "italic underline"))
# en = canvas.create_text(400, 300, text="", font=("ariel", 40, ""))

# #$ Wrong Button:
# wrong = PhotoImage(file="python projects/Level B projects/24 project folder B/project files/wrong_button.png")
# button_wrong = Button(image=wrong, highlightthickness=0)
# button_wrong.config(activebackground="dark slate gray", overrelief="sunken", command=next_card)
# button_wrong.grid(column=0, row=1)

# #$ Correct Button:
# right = PhotoImage(file="python projects/Level B projects/24 project folder B/project files/right_button.png")
# button_right = Button(image=right, highlightthickness=0)
# button_right.config(activebackground="dark slate gray", overrelief="ridge", command=known)
# button_right.grid(column=1, row=1)

# next_card()
# window.mainloop()