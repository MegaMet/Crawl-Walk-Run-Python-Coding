#Password manager Project

from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    #Select the requested amount of charaters from each list
    list_of_letters = [choice(letters) for i in range(randint(8, 10))]
    list_of_symbols = [choice(symbols) for i in range(randint(2, 4))]
    list_of_numbers = [choice(numbers) for i in range(randint(2, 4))]

    #combine the 3 list of strings into 1 string.
    randomized_password = list_of_letters + list_of_symbols + list_of_numbers
    shuffle(randomized_password)
    randomized_password = "".join(randomized_password)

    entry_password.delete(0, END)
    entry_password.insert(0, randomized_password)
    pyperclip.copy(randomized_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = entry_website.get()
    username = entry_username.get()
    password = entry_password.get()

    if len(password) == 0 or len(username) == 0 or len(website) == 0:
        messagebox.showinfo(title= "Opps", message= "Please fill out all fields")
    else:
        is_ok = messagebox.askokcancel(title= website, message= f"These are the details entered: \n\nEmail/Username: {username} \n Password: {password} \n\nIs this OK?")

    if is_ok:
        with open("data.txt", "a") as data_file:
            data_file.write(f"{website}\n{username}\n{password}\n\n")

            entry_password.delete(0, END)
            entry_website.delete(0, END)
            entry_website.focus_set()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx= 20, pady= 20)

canvas = Canvas(height= 200, width= 200)
logo_img = PhotoImage(file= "logo.png")
canvas.create_image(100, 100, image= logo_img)
canvas.grid(row= 0, column= 1)

#Labels
label_website = Label(text= "Window:")
label_website.grid(row= 1, column= 0)

label_username = Label(text= "Email/Username:")
label_username.grid(row= 2, column= 0)

label_password = Label(text= "Password:")
label_password.grid(row= 3, column= 0)

#Entry Fields
entry_website = Entry(width= 50)
entry_website.grid(row=1, column= 1, columnspan= 2)

entry_username = Entry(width= 50)
entry_username.grid(row=2, column= 1, columnspan= 2)
entry_username.insert(0, "example@email.com")

entry_password = Entry(width= 32)
entry_password.grid(row=3, column= 1)

#Buttons
button_generatepw = Button(text= "Generate Password", command= generate_password)
button_generatepw.grid(row= 3, column=2)

button_add = Button(text= "Add", width= 43, command= save)
button_add.grid(row= 4, column=1, columnspan= 2)

entry_website.focus_set()

window.mainloop()