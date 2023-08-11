from tkinter import *

my_window = Tk()
my_window.title("Mile to Km Converter")
#my_window.minsize(width=400, height=200)
my_window.config(padx=40, pady=30)


def convert():
    miles = float(user_input.get())
    km = miles * 1.609
    my_label3.config(text=f"{km}")


user_input = Entry(width=7)
user_input.get()
user_input.grid(column=1, row=0)

my_label = Label(text="Miles")
my_label.grid(column=2, row=0)

my_label2 = Label(text="is equal to")
my_label2.grid(column=0, row=1)

my_label3 = Label(text="")
my_label3.grid(column=1, row=1)

my_label4 = Label(text="Km")
my_label4.grid(column=2, row=1)

button = Button(text="Click me", command=convert)
button.grid(column=1, row=2)


my_window.mainloop()