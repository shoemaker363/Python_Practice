import pandas
data = pandas.read_csv("python projects/Level B projects/24 project folder/nato_phonetic_alphabet.csv")

#!      Phonetic Alphabet with exception
# TODO: Create a dictionary in this format.
# TODO: Create a list of the phonetic code words from a word that the user inputs.
# TODO: Catch an exception from user input.
#?          Example: User inputs 123123.
#* Solution starts on line 100.


























































































# phonetic = {row.letter: row.code for (index, row) in data.iterrows()}
# print(phonetic)


# def encode():    
#     word = input("Enter a word: ").upper()
#     try:
#         output = [phonetic[letter] for letter in word]
#     except KeyError:
#         print("Sorry only letters in the alphabet please.")
#         encode()     
#     else:
#         print(output)
# encode()