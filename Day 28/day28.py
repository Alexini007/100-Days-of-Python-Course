from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
import time
def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        my_window.after(1000, count_down, count - 1)  # 1000 is milliseconds = 1 sec

def start_timer():
    count_down(2500)


# ---------------------------- UI SETUP ------------------------------- #
my_window = Tk()
my_window.title("Pomodoro")
my_window.config(padx=100, pady=50, bg=YELLOW)



canvas = Canvas(width=210, height=224, bg=YELLOW, highlightthickness=0)
my_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=my_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(column=1, row=1)


label_title = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 35, "bold"), bg=YELLOW)
label_title.grid(column=1, row=0)

button_start = Button(text="Start", bg=YELLOW, highlightthickness=0, command=start_timer)
button_start.grid(column=0, row=2)

button_reset = Button(text="Reset", bg=YELLOW, highlightthickness=0)
button_reset.grid(column=3, row=2)

label_checkmark = Label( text="✔️", fg=GREEN, bg=YELLOW)
label_checkmark.grid(column=1, row=3)


my_window.mainloop()