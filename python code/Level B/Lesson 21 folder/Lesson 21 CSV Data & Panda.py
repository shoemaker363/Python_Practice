
# #! CSV Data.
#         #? CSV = Comma Seperated Values.
#         #? Ex. Weather_data.csv.
#         #? Each row is a single set of data. 
#         #? Each piece of Data is seperated by a Comma.

# #! producing a list of data from weather_data.
# with open("python code/Level B/Lesson 21 folder/weather_data .csv") as data_file:
#     data = data_file.readlines()
#     print(data)


# #! CSV reader.

# import csv

# with open("python code/Level B/Lesson 21 folder/weather_data .csv") as data_file:
#     data = csv.reader(data_file)                                                ## Reads data from 'weather_data.csv'.
#     for row in data:                                                            ## Processing the data by each Row.
#         print(row)                                                              ## Prints each Row on new lines.

# #! CSV reader to acces temperatures and make into python list.

# import csv

# with open("python code/Level B/Lesson 21 folder/weather_data .csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for column in data:
#         if column[1] != "temp":
#             temperatures.append(int(column[1]))
#     print(temperatures)

# #! Using Panda Library to make reading and using 'weather_data.csv' easier.
#           #@ Panda Documentation: https://pandas.pydata.org/docs/
#           #@ Panda API reference: https://pandas.pydata.org/docs/reference/index.html

# import pandas

# data = pandas.read_csv("python code/Level B/Lesson 21 folder/weather_data .csv")
# print(data)                                                                     ## Prints as a more ledgible table.
#                                                                                 ## Provides Header at the top of each Column.
#                                                                                 ## Provides an Index number for each Row.

# #! Using Pandas to access temperature Column and make into a python list.

# import pandas

# data = pandas.read_csv("python code/Level B/Lesson 21 folder/weather_data .csv")
# print(data["temp"])                                                             ## Identifies the first Row to be Header names for each Column.
#                                                                                 ## Uses information to select the data provided in Column.
#                                                                                 ## Provides an Index number for each Row and the data from the Column you are wanting.

# #! Pandas Dataframe and Pandas Series.
#         #? Dataframe: The entire file data you are using pandas to read.
#         #? Series: A single Column of data you are using pandas to read.

# import pandas

# data = pandas.read_csv("python code/Level B/Lesson 21 folder/weather_data .csv")
# print(type(data))                                                               ## DataFrame.
# print(type(data["temp"]))                                                       ## Series.

# #! Pandas Dictionary.

# import pandas

# data = pandas.read_csv("python code/Level B/Lesson 21 folder/weather_data .csv")
# dictionary = data.to_dict()                                                     ## Pulls each Column to be processed as list.
# print(dictionary)                                                               ## Each Column will print with Header to start and a list of Data from that Column along with Index number to identify what Row.

# #! Pandas List.

# import pandas

# data = pandas.read_csv("python code/Level B/Lesson 21 folder/weather_data .csv")
# list = data["temp"].to_list()                                                   ## Pulls Column Data based on Header name provided.
# print(list)                                                                     ## Prints a list of the Column Data.

# #! Pandas list works well with Python Functions.

# import pandas

# data = pandas.read_csv("python code/Level B/Lesson 21 folder/weather_data .csv")
# list = data["temp"].to_list()
# print(len(list))                                                                ## Length of list.

# average = sum(list) / len(list)                                                 ## Sum of all temperatures divided by length of list.
# print(average)                                                                  ## Average temperature.

# #! Some Pandas Functions.

# import pandas

# data = pandas.read_csv("python code/Level B/Lesson 21 folder/weather_data .csv")
# list = data["temp"].to_list()
# print(len(list))

# print(data["temp"].mean())                                                      ## Print the Average temperature.
# print(data["temp"].median())                                                    ## Prints the Middle number from list provided.
# print(data["temp"].max())                                                       ## Prints the Maximum number from list provided.
# print(data["temp"].min())                                                       ## Prints the Minimum number from list provided.
# print(data["temp"].sum())                                                       ## Prints the Sum of all numbers in list provided.

# #! 2 way to access Column Data with Pandas.
#         #? 1) ["temp"] = string method.
#         #? 2) data.temp = Calling method.

# import pandas

# data = pandas.read_csv("python code/Level B/Lesson 21 folder/weather_data .csv")

# print(data["temp"])                                                             ## String method.

# print(data.temp)                                                                ## Calling method.

# #! Getting Data from a Row using Pandas.

# import pandas

# data = pandas.read_csv("python code/Level B/Lesson 21 folder/weather_data .csv")
# print(data[data.day == "Monday"])                                               ## Prints the Row for 'Monday.

# #! Finding a specific variable, and provides Row Data.

# import pandas

# data = pandas.read_csv("python code/Level B/Lesson 21 folder/weather_data .csv")
# print(data[data.temp == data.temp.max()])                                       ## Finds and Prints the Row that has the highest temperature.

#! Takes a specific Row, and prints the wanted variable.

# import pandas

# data = pandas.read_csv("python code/Level B/Lesson 21 folder/weather_data .csv")

# monday = data[data.day == "Monday"]                                             ## Retrieves Data for Row 'Monday'.
# print(monday.condition)                                                         ## Prints the 'condition' Header Column for Row 'Monday'.

# #! Creating a Dataframe.

# import pandas

# dictionary = {
#     "domnick": ["d", "o", "m", "n", "i", "c", "k"],                             #* I'm aware I spelled the name wrong.
#     "protute": ["p", "r", "o", "t", "u", "t", "e"]
# }

# data = pandas.DataFrame(dictionary)                                             ## Dictionary becomes the Dataframe for Pandas.
# print(data)
# data.to_csv("python code/Level B/Lesson 21 folder/the_pro.csv")                 ## Makes a CSV file with the Dictionary data.