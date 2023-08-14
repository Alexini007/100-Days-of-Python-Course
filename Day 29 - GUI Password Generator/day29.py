from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
               'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
               'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for n in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for n in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for n in range(random.randint(2, 4))]
    password_list = password_letters + password_numbers + password_symbols

    random.shuffle(password_list)

    password = "".join(password_list)   #!!! join function
    password_input.delete(0, END)
    password_input.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_an_entry():
    website = website_input.get()
    username = username_input.get()
    password = password_input.get()

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showinfo(message="Please don't leave empty field")

    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are the details entered: \nEmail:{username} \nPassword: "
                                               f"{password} \nIs it ok to save?")
        if is_ok:
            with open("data.txt", mode="a") as data:
                data.write(f"{website} | {username} | {password}\n")
                website_input.delete(0, END)
                username_input.delete(0, END)
                password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
my_window = Tk()
my_window.title("Password Manager")
my_window.config(padx=50, pady=50)

canvas = Canvas(width=210, height=258)
my_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=my_image)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:", font=("Arial", 11), padx=10)
website_label.grid(column=0, row=1, sticky="e")

username_label = Label(text="Email/Username:", font=("Arial", 11), padx=10)
username_label.grid(column=0, row=2, sticky="e")

password_label = Label(text="Password:", font=("Arial", 11), padx=10)
password_label.grid(column=0, row=3, sticky="e")

website_input = Entry(width=52)
website_input.focus()
website_input.grid(column=1, row=1, columnspan=2, sticky=EW)

username_input = Entry(width=52)
username_input.grid(column=1, row=2, columnspan=2, sticky=EW)

password_input = Entry(width=33)
password_input.grid(column=1, row=3, sticky=EW)

generate_button = Button(text="Generate password", command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=44, command=save_an_entry)
add_button.grid(column=1, row=4, columnspan=2, sticky=EW)

my_window.mainloop()
