
#! Advanced Python Argument
#$  Keyword Argument:
#?      def function(A, B, C):
#*          A = This.
#*          B = Then B is This.
#*          C = Finally C is This.

#?      function(A=1, B=2, C=3) 
#*          Calling the 'function' is where Arguments get changed.
#*          EX. Can change 'A=1' to 'A=2' when calling 'function' and now A is processed as 2.

#$  Unlimited Arguments:
#?      def function(*args):
                                                                    ## ' * ': Tells python the function can accept any number of arguments.
#*          for n in args:
#*              print(n)

#$ Example Unlimited Arguments:
#?      ' * ': Required portion for Unlimited Arguments.
#?      'args': Optional variable name, but args is the standard variable name to use.

def add(*args):                                                     ## ' * ': Unlimited arguments
    sum = 0
    for n in args:
        sum += n
    return sum

print(add(10, 10 , 10, 10, 10, 10, 10, 10, 10, 9))

#$ Example of Unlimited Keyword Arguments:
#?      ' ** ': Required portion intiate unlimited Keyword Arguments.
#?      'kwargs': Optional variable name, but kwargs is the standard variable name to use.

def calculate(n, **kwargs):                                         ## ' ** ': Unlimited Keyword arguments
    print(kwargs)

    n += kwargs["add"]                                              ## '["add"]': New variable added to Keyword Argument.
    n *= kwargs["multiply"]                                         ## '["multiply"]: New variable added to Keyword Argument.
    print(n)

calculate(2, add=3, multiply=5)

#$ Example class with Unlimited Keyword arguments:
#?      Keyword Arguments uses brackets for each variable being added.

class Big_business:

    def __init__(self, **kw):
        self.company = kw["company"]
        self.employees = kw["employees"]

new_company = Big_business(company = "Protute", employees = 1)

print(f"New company name is {new_company.company} and there is {new_company.employees} employees.")

#$ Example class with Unlimited Keyword arguments and none returned as a response:
#?      'get' method requires parenthesis to use.

class Big_business:

    def __init__(self, **kw):
        self.company = kw.get("company")## 'get': if key doesn't exist returns None as a response.
        self.ceo = kw.get("ceo")
        self.employees = kw.get("employees")

new_company = Big_business(company = "Protute", employees = 1)

print(f"New company name is {new_company.company} with the CEO being {new_company.ceo} and there is {new_company.employees} employees.")

#! Tkinter

#@      Text fonts: python code/Level B/Lesson 23 folder/tkinter_fonts.py
#@      Text Colors: https://cs111.wellesley.edu/archive/cs111_fall14/public_html/labs/lab12/tkintercolor.html
#@      The Packer: https://docs.python.org/3/library/tkinter.html#the-packer
#@      Tk class docs: https://www.tcl-lang.org/man/tcl8.6/TkCmd/pack.htm

#?      Used to make a GUI.
#*          GUI: Graphical User Interface.
#?      GUI allow a user to click on a object on monitor and have a result.
#?      TK reads and interprets profile files into the Tcl interpreter and calls exec().
#?      Modules that support Tk include:
#*          tkinter: Main Tkinter module.
#*          tkinter.colorchooser: Dialog to let user choose a color.
#*          tkinter.commondialog: Base Class for dialogs defined in other modules listed.
#*          tkinter.filedialog: Common dialogs to allow user to specify file to open or save.
#*          tkinter.font: Utilities to help work with fonts.
#*          tkinter.messagebox: Access to standard Tk dialog boxes.
#*          tkinter.scrolledtext: Text widget with a vertical scroll bar built in.
#*          tkinter.simpledialog: Basic dialogs and convenience functions.
#*          tkinter.ttk: Themed widget set provides modern alternatives for many classic widgets.
#*

#! Creating a Window

import tkinter 
#?      Alternate option is:
#*          - | from tkinter import * |.
#*          ' * ': Pulls all classes from 'tkinter'.
#*          With all classes pulled you don't have to write 'tkinter.Class()', you would just type the Class.

#$ Example Window creation and modifications:
window = tkinter.Tk()                                           ## 'Tk()': Can have in parenthesis (1,2,3,4,5,6): 
                                                                ##        1) screenName (str): Sets display environment variable.
                                                                ##        2) baseName (str): Name of the profile file.
                                                                ##        3) className (str): Name of the widget class.
                                                                ##        4) useTk (boolean): If True, initializes the Tk subsystem.
                                                                ##        5) sync (boolean): If True, execute all X server commands synchronously.
                                                                ##        6) use (str): Specifies the ID of the window in which to embed the app.

window.title("Title bar")                                       ## 'title()': Puts the string on the window title bar.

window.minsize(width=500, height=500) 
                                                                ## 'minsize': Changes starting size of the window.

window.config(padx=20, pady=20)                                 ## 'padx=20, pady=20': Provides space between edge of screen and working space.

#$ Labels inside the Window:
label = tkinter.Label(text="This is a label.", font=("Arial", 24, "bold")) 
                                                                ## Option 1 to add text and how it looks.

label.pack(side="bottom")                                       ## 'pack': Displays the Label on the screen in the created window.

label["text"] = "Newer Label Text"                              ## 'label["text"]': Option 2 to change displayed text.

label.config(text="Newest Label Text")                          ## 'label.config': Option 3 to change disdplayed text.

#$ Buttons in the Window:
def push_button():
    print("Dom touched the butt!")

button = tkinter.Button(text="Button Here", command=push_button)
                                                                ## 'Button'(): Creates the button.
                                                                ## 'text': What the button has written on it.
                                                                ## 'command': Name of function you want to use, Not calling the function so don't need paranthesis at the end of function name.

button.pack(side="right")                                       ## 'pack': Displays the Button on the screen in the created window.

#$ Button with Label printed changing after click:
label2 = tkinter.Label(text="Dom", font=("Rockwell", 30))
label2.pack()

def label_button():
    label2.config(text="Dom Touched The Butt! 🤯")
    
button2 = tkinter.Button(text="Don't Push The Button", command=label_button)

#$ Place method instead of pack:
#?      EX. button2.place(x=0, y=0)
button2.place(x=0, y=400)                                       ## 'x=0, y=0': Based off the size tkinter screen.

#$ Entry Class:
def button3_pressed():
    input_text = input.get()
    label.config(text=input_text)                               ## Uses the input text as the new text.

button3 =tkinter.Button(text="Try typing something first.", command=button3_pressed)
button3.pack(side="left")

input = tkinter.Entry(width=10)                                 ## 'Entry': Makes a input bar.
                                                                ## 'width': Horizontal length of input bar.

input.pack(side="left")

#$ Text:
text = tkinter.Text(height=5, width=30)

text.focus()                                                    ## Puts cursor in text box.

text.insert(tkinter.END, "Example for multi-line entry box")    ## Starting text.
print(text.get("1.0", tkinter.END))

text.pack()

#$ Spinbox:
def spinbox_used():
    print(spinbox.get())                                        ## Prints current value of spinbox.

spinbox = tkinter.Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

#$ Scrollbar:
def scale_used(value):
    print(value)                                                ## Prints current value of scrollbar

scale = tkinter.Scale(from_=0, to=100, command=scale_used)
scale.pack()

#$ Radiobutton:
def radio_used():
    print(radio_state.get())

radio_state = tkinter.IntVar()

#$ Different valued radio buttons:
radiobutton1 = tkinter.Radiobutton(text="Option 1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = tkinter.Radiobutton(text="Option 2", value=2, variable=radio_state, command=radio_used)

radiobutton1.pack()
radiobutton2.pack()

#$ Listbox:
def listbox_used(event):
    print(listbox.get(listbox.curselection()))

listbox = tkinter.Listbox(height=4)
fruits=["Apple", "Pear", "Orange", "Banana"]                    ## Different items in listbox

for item in fruits:
    listbox.insert(fruits.index(item), item)

listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()



window.mainloop()                                               ## 'mainloop()': Puts everything of the display and responds to user inputs.

#$ Grid method of placing objects:
#?  Splits the screen into columns and rows.
#?  Starts at top left of window.

        #* EX. listbox.grid(column=0, row=0)

#?  Change column for horizontal movement across the window.
#?  Change row for vertical movement across the window.

#?  Can not use Pack and Grid in the same in program.