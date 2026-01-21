import math
from tkinter import *

#! Pomodoro Technique timer

#?      Step 1: Decide on task to be completed.
#?      Step 2: Set a timer to 25 minutes.
#?      Step 3: Work on task until timer goes off.
#?      Step 4: Take a 5 minute break.
#*          Complete steps 1 - 4 four times.
#?      Step 5: Take a 15 - 30 minute break.

#! Python Strongly, Dynamically typing
#?      Strong: The type of a value doesn't change in unexpected ways. 
#?              A string containing only digits doesn't magically become a number, 
#?              as may happen in Perl. Every change of type requires an explicit conversion.

#?      Dynamic: Runtime objects (values) have a type, as opposed to static typing where variables have a type.
#@      More information on strong and dynamic typing: https://stackoverflow.com/questions/11328920/is-python-strongly-typed

#$ Constants:
PINK = "#f518a0"
RED = "#db0a0a"
GREEN = "#06a82e"
YELLOW = "#f3e249"

FONT_NAME = "Times New Roman"
WORK = 25
SHORT = 5
LONG = 20
rep = 0
counter = None

#$ UI setup:
window = Tk()
window.title("Timer")
window.config(padx=50, pady=50, bg=YELLOW)                                      ## 'bg': Background color.

#$ Reset Button Configuration:
def reset_time():
    global rep
    rep = 0
    window.after_cancel(counter)
    itteration.config(text="")
    canvas.itemconfig(timer, text="00:00")
    label_TI.config(text="Timer", fg=GREEN)
    
#$ Timer Setup:
def timer_start():
    global rep
    rep += 1
    if rep % 8 == 0:
        countdown(LONG * 60)
        label_TI.config(text="Rest Time", fg=RED)
    elif rep % 2 == 0:
        countdown(SHORT * 60)
        label_TI.config(text="Break", fg=PINK)
    else:
        countdown(WORK * 60)
        label_TI.config(text="Working", fg=GREEN)

def countdown(count):
    minutes = math.floor(count / 60)
    seconds = count % 60

   
#$ Adding a 0 to single digit numbers in timer:
#?      An example of Dynamic typing.     
    if seconds < 10:
        seconds = f"0{seconds}"

    canvas.itemconfig(timer, text=f"{minutes}:{seconds}")
    if count > 0:
        global counter
        counter = window.after(1000, countdown, count -1)
    else:
        timer_start()
        mark = ""
        session = math.floor(rep/2)
        for _ in range(session):
            mark += "☣"
        itteration.config(text=mark)

#$ Program Title:
label_TI = Label(text="Timer", fg=GREEN, bg=YELLOW, font=("Times New Roman", 45, ""))
label_TI.grid(column=1, row=0)

#$ Canvas:
#?      Allow for items to be stacked on top of each other.
#?      Canvas only natively accepts .gif files for images.
canvas = Canvas(width=230, height=230, highlightthickness=0)                    ## 'highlightthickness': Border of image.

photo = PhotoImage(file="python code/Level B/Lesson 23 folder/hour_glass.gif")  ## Loads image file .

canvas.create_image(115, 115, image=photo)                                      ## Inputs image at x,y coordinates.

timer = canvas.create_text(115, 115, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

#$ Starting Button:
button_ST = Button(text="Start", font=(FONT_NAME, 12, "bold"), command=timer_start)
button_ST.grid(column=0, row=3)

#$ Reset Button:
button_RE = Button(text="Reset", font=(FONT_NAME, 12, "bold"), command=reset_time)
button_RE.grid(column=2, row=3)

#$ Itteration Tracker:
#@  For different options of symbols: https://www.alt-codes.net/ 
itteration = Label(fg=RED, bg=YELLOW, font=(FONT_NAME, 25, ""))
itteration.grid(column=1, row=3)

#$ Keep window open:
window.mainloop()