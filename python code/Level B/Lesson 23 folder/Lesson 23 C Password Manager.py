import pyperclip
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle

#! Password Manager

#$ Password Generation:
def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pass_letters = [choice(letters) for _ in range(randint(8,10))]
    pass_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    pass_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = pass_numbers + pass_letters + pass_symbols
    
    shuffle(password_list)

#$ Joining of string:
#@      Documentation: https://www.w3schools.com/python/ref_string_join.asp
    new_password = "".join(password_list)

    text_p.insert(0, f"{new_password}")

#$ Copy Password:
#?      Pyperclip can automatically copy a string for a user, so they can paste it else where.
#@      Documentation: https://pypi.org/project/pyperclip/
    pyperclip.copy(new_password)

#$ Save Password:
def save_p():
    website = text_w.get()
    username = text_u.get()
    password = text_p.get()

#$ Checks if all text boxes are filled:
    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showwarning("Error", "Please fill out all information.")
    
#$ Checks if user wants to proceed with saving data:
#?      Python file write is used to write information to text file.
#@      Documentation: https://www.w3schools.com/python/python_file_write.asp
    else:
        proceed = messagebox.askokcancel(title=website, message=f"Information being saved:\nWebsite: {website}\nUsername/Email: {username}\nPassword: {password}\n Proceeding saves information.")

        if proceed:
            with open("python code/Level B/Lesson 23 folder/data.txt", "a") as data_file:
                data_file.write(f"{website} | {username} | {password}\n")
                text_w.delete(0, END)
                text_p.delete(0, END)

#$ Window Configuration:
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

#$ Canvas Configuration:
#@      Documentation: https://tkdocs.com/tutorial/canvas.html
canvas = Canvas(width=300, height=300)
photo = PhotoImage(file="python code/Level B/Lesson 23 folder/manager.gif")
canvas.create_image(165, 110, image=photo)
canvas.grid(column=0, row=0, columnspan=3)

#$ Website:
label_w = Label(text="Website:")
text_w = Entry(width=43)
text_w.focus()
label_w.grid(column=0, row=1, sticky=E)                         ## 'sticky': Aligns variable along the cardinal direction chosen.
text_w.grid(column=1, row=1, columnspan=2, sticky=W)

#$ Username/Email:
label_u = Label(text="Username/Email:")
text_u = Entry(width=43)
text_u.insert(0, "dom.protute@yahoo.com")                       ## 'insert': Inputs a string into entry box.
label_u.grid(column=0, row=2, sticky=E)
text_u.grid(column=1, row=2, columnspan=2, sticky=W)

#$ Password:
label_p = Label(text="Password:")
text_p = Entry(width=21)
button_p = Button(text="Password Generator", command=generate)
label_p.grid(column=0, row=3, sticky=E)
text_p.grid(column=1, row=3, sticky=W)
button_p.grid(column=2, row=3, sticky=E)

#$ Confirmation
button_c = Button(text="Confirm", width=36, height=1, command=save_p)
button_c.grid(column=1, row=4, columnspan=2, sticky=W)

window.mainloop()