from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"
FONT_NAME = "Arial"
TRUE_COLOR = "#b3ffb3"
FALSE_COLOR = "#ff8080"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain ):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125,
                                                     text="Score: 0",
                                                     fill=THEME_COLOR,
                                                     width=280,
                                                     font=(FONT_NAME, 16, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50, padx=20)

        self.score_label = Label(text="Score: 0", font=("Arial", 11), bg=THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0)

        yes_image = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=yes_image, text="", highlightthickness=0, command=self.press_true, bd=0)
        self.true_button.grid(column=0, row=2)

        no_image = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=no_image, text="", highlightthickness=0, command=self.press_false, bd=0)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def press_true(self):
        self.flash_answer(self.quiz.check_answer("True"))

    def press_false(self):
        self.flash_answer(self.quiz.check_answer("False"))

    def flash_answer(self, is_right):
        if is_right:
            self.canvas.config(bg=TRUE_COLOR)
        else:
            self.canvas.config(bg=FALSE_COLOR)
        self.window.after(1000, self.get_next_question)
