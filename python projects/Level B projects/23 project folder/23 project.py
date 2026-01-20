
#!      Make a mile to kilometer conversion calculator.

# TODO: Make a window with tkinter.
# TODO: Make labels for 'kilometer' and 'mile'.
# TODO: Have a way for user to input miles they want converted.
# TODO: Make a button to start calculation.
# TODO: Make a function that converts mile to kilometers
#?              conversion equation: miles * 1.609
# TODO: Have result appear in the window.

#* Solution starts on line 100.























































































# from tkinter import *

# #$ Window creation
# window = Tk()
# window.title("Conversion calculator")
# window.minsize(width=300, height=300)
# window.config(padx=50, pady=50)

# #$ Function to calculate:
# def calculator():
#     input_num = float(input.get())
#     km_result = input_num * 1.609
#     labelkm.config(text=f"{km_result}")

# #$ Heading:
# label = Label(text="Input miles to convert")
# label.grid(column=1, row=0)
# label.config(padx=10, pady=10)

# #$ Kilometer row:
# labelkm2 = Label(text="Kilometers")
# labelkm2.grid(column=0, row=3)
# labelkm2.config(padx=10, pady=10)
# labelkm = Label(text="Result")
# labelkm.grid(column=2, row=3)
# labelkm.config(padx=10, pady=10)

# #$ Button row:
# button = Button(text="calculate", command=calculator)
# button.grid(column=2, row=2)
# button.config(padx=10, pady=10)
# labelbt = Label(text="=")
# labelbt.grid(column=0, row=2)
# labelbt.config(padx=10, pady=10)

# #$ Input row:
# input = Entry(width=10)
# input.grid(column=2, row=1)
# labelin= Label(text="Miles")
# labelin.grid(column=0, row=1)
# labelin.config(padx=10, pady=10)

# #$ Keep window open:
# window.mainloop()