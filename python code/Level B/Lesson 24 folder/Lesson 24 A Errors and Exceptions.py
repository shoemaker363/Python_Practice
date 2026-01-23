
#! Catching Exceptions
#@      Errors documentation: https://docs.python.org/3/tutorial/errors.html
#@      Exception documentation: https://docs.python.org/3/library/exceptions.html#Exception
#?      Keywords that handle exceptions:
#*          'try': You are trying to execute a piece of code that MIGHT cause and exception.
#*          'except': If an exception occurs, do this.
#*          'else': If no exceptions occur, do this.
#*          'finally': Do this regardless of what happens.
#*          'raise': Forces a specific exception to occur.

# #$ FileNotFound error example:
# #?      Terminal text of error: (FileNotFoundError: [Errno 2] No such file or directory: 'a_file.txt')
# with open("a_file.txt") as file:
#     file.read()

#$ Try example:
try:                                                    ## Requires either 'except' or 'finally' to follow.
    file = open("python code/Level B/Lesson 24 folder/a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["key"])

#$ Except example:
#?      Be specific with what errors you are trying to use except on.
except FileNotFoundError:                               ## 'FileNotFoundError': Used to specify error we are trying to get past.
    file = open("python code/Level B/Lesson 24 folder/a_file.txt", "w")
    file.write("Dom is a ProTute!")  
    print("try has failed.")

#$ Except example with error message:
#?      Useful for when there is a value that causes an error.
except KeyError as error_message:                           ## Changing the string 'key' on line 20 will produce this error.
    print(f"The key {error_message} does not exist.")

#$ Else example:
else:
    content = file.read()
    print((content))

#$ Finally example:
finally:
    file.close()
    print("File closed.")

# #$ Raise example:
# #?      Leave commented out unless you want to run this particular code.
# height = float(input("Height in Inches: "))
# weight = int(input("Weight in Pounds: "))

# if height > 96:
#     raise ValueError("Most human height should not be over 96 inches")

# bmi = (weight / height ** 2) * 703
# print(bmi)

#$ Function with Exception catching:
facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]

def count_likes(posts):
   
    total_likes = 0
    for post in posts:
        try:                                            ## Attempting to run through each dictionaries likes to add them together.
            total_likes = total_likes + post['Likes']
            
        except KeyError:                                ## If dictionary does not have like, skips over that dictionary.
            pass
    
    print(total_likes)
    return total_likes

count_likes(facebook_posts)

#$ Function with Exception catching 2:
fruits = ["Apple", "Pear", "Orange"]
 
def make_pie(index):
  try:                                                  ## Attempts to locate the index provided.
    fruit = fruits[index]
  except IndexError:                                    ## If provided index is out of range.
    print("Fruit pie Dom!")
  else:                                                 ## If provided index is in range.
    print(fruit + " pie")
 
make_pie(4)