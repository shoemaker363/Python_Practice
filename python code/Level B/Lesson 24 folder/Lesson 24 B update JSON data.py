import pyperclip
import json
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle

#! Password Manager Version 2.0


def generate():                                                                                                         ## Password Generation:
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pass_letters = [choice(letters) for _ in range(randint(8,10))]
    pass_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    pass_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = pass_numbers + pass_letters + pass_symbols   
    shuffle(password_list)

    new_password = "".join(password_list)                                                                               ## Joining of string:
    text_p.insert(0, f"{new_password}")
    pyperclip.copy(new_password)                                                                                        ## Copy Password:


def save_p():                                                                                                           ## Save Password:
    website = text_w.get()
    username = text_u.get()
    password = text_p.get()

#! JSON
#@      Documentation: https://docs.python.org/3/library/json.html
#?      JSON Basic Usage:
#*          json.dump: Serialize Python object as a JSON formatted stream to file-like-object.
#*          json.load: Deserialize file-like-object to a Python object.
#*          json.loads: Deserializes a string, bytes or bytearray instance containing a JSON document to a Python object.

#$ Format when saved to JSON file:
    new_data = {
        website: {
            "email": username,
            "password": password
        }
    }

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showwarning("Error", "Please fill out all information.")

#$ Saving to JSON file:    
    else:

#?  Tries to Open and Read JSON file in Python:       
        try:
            with open("python code/Level B/Lesson 24 folder/data.json", "r") as data_file:
                data = json.load(data_file)                                                 #// Reads old data in JSON file.

#?  If JSON file doesn't exist or can't be found, make a new JSON file with the new data:                
        except FileNotFoundError:
            with open("python code/Level B/Lesson 24 folder/data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)                                    #//  Makes new JSON file and saves new data.

#?  If JSON file does exist and is found, update Pythons old data with the new data:
        else:
            data.update(new_data)                                                           #// Updates the old data with new data.

#?  Once old data is updated with new data, save the updated data to the JSON file:        
            with open("python code/Level B/Lesson 24 folder/data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)                                        #// Saves the updated data.

        finally:
            text_w.delete(0, END)
            text_p.delete(0, END)

#$ Searching for data with JSON:
def searching():
    website = text_w.get()

#?  Tries to open JSON data file:
    try:
        with open ("python code/Level B/Lesson 24 folder/data.json") as data_file:
            data = json.load(data_file)

#?  If JSON file doesn't exist or can't be found, makes a new window to notify user.
    except FileNotFoundError:
            messagebox.showinfo(title="Error", message="No data file found.")

#?  If JSON file does exist and can be found, looks through data for information requested and displays in new window.
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        
#?  If data user is looking for can't be found in the data, displays a window notifying user there is no saved data.        
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} have been saved.")


window = Tk()                                                                                                           ## Window Configuration:
window.title("Password Manager")
window.config(padx=60, pady=50, bg="Red3")


label_title = Label(text="Password Manager Version 2.0", font=("Times New Roman", 20, "bold"), fg="midnight blue", bg="red3")
label_title.grid(column=0, columnspan=3, sticky=W)
label_title.config(padx=110)


canvas = Canvas(width=400, height=300, borderwidth=0, highlightthickness=0, bg="red3")                                  ## Window Configuration:
photo = PhotoImage(file="python code/Level B/Lesson 24 folder/manager 2.0.gif")
canvas.create_image(220, 150, image=photo)
canvas.grid(column=0, row=1, columnspan=3)


label_w = Label(text="Website:", font=("Freestyle Script", 20, "bold"), borderwidth=0, fg="darkgoldenrod1", bg="red3")  ## Website:
label_w.config(width=10, pady=10)
text_w = Entry(width=38)
text_w.focus()
button_w = Button(text="Search", command=searching)
button_w.config(padx=10, width=20)
label_w.grid(column=0, row=2, sticky=W)                        
text_w.grid(column=1, row=2, sticky=W)
button_w.grid(column=2, row=2, sticky=E)


label_u = Label(text="Username/Email:", font=("Freestyle Script", 20, "bold"), fg="darkgoldenrod1", bg="red3")          ## Username/Email:
label_u.config(width=15, pady=10)
text_u = Entry(width=68)
text_u.insert(0, "ProTute.Dom@AOL.com")                       
label_u.grid(column=0, row=3, sticky=W)
text_u.grid(column=1, row=3, sticky=W, columnspan=2)


label_p = Label(text="Password:", font=("Freestyle Script", 20, "bold"), fg="darkgoldenrod1", bg="red3")                ## Password:
label_p.config(width=10, pady=12)
text_p = Entry(width=38)
button_p = Button(text="Password Generator", command=generate)
button_p.config(padx=10, width=20)
label_p.grid(column=0, row=4, sticky=W)
text_p.grid(column=1, row=4, sticky=W)
button_p.grid(column=2, row=4, sticky=E)


button_c = Button(text="Confirm", width=32, height=1, command=save_p)                                                   ## Confirmation
button_c.grid(column=1, row=5, sticky=W)

window.mainloop()