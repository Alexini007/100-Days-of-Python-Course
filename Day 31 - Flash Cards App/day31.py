from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    my_window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=front_card_image)
    flip_timer = my_window.after(3000, func=flip)

def flip():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=back_card_image)


def is_known():
    to_learn.remove(current_card)
    next_card()
    learn_data = pandas.DataFrame(to_learn)
    learn_data.to_csv("./data/words_to_learn.csv", index=False)


my_window = Tk()
my_window.title("Flashy")
my_window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


flip_timer = my_window.after(3000, func=flip)

canvas = Canvas(width=800, height=526)
front_card_image = PhotoImage(file="./images/card_front.png")
back_card_image = PhotoImage(file="./images/card_back.png")
card_background = canvas.create_image(400, 263, image=front_card_image)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 30, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 50, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

no_image = PhotoImage(file="./images/wrong.png")
no_button = Button(image=no_image, highlightthickness=0, command=next_card)
no_button.grid(column=0, row=1)

yes_image = PhotoImage(file="./images/right.png")
yes_button = Button(image=yes_image, highlightthickness=0, command=is_known)
yes_button.grid(column=1, row=1)

next_card()



my_window.mainloop()