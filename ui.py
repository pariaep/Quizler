from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuestionGame:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR, height=600, width=400)

        self.canvas = Canvas()
        self.canvas.config(height=250, width=300, bg="white", highlightthickness=0)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.question_text = self.canvas.create_text(150, 125, text="hello", fill=THEME_COLOR,
                                                     width=280, font=("Arial", 20, "italic"))

        true = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=true, highlightthickness=0, bg=THEME_COLOR, borderwidth=0, command=self.true_pressed)
        self.true_button.grid(column=0, row=2)

        false = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=false, highlightthickness=0, bg=THEME_COLOR, borderwidth=0, command=self.false_pressed)
        self.false_button.grid(column=1, row=2)

        self.score = Label(text="Score:0", bg=THEME_COLOR)
        self.score.grid(column=1, row=0)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You finished the quiz!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        answer = self.quiz.check_answer("true")
        self.give_feedback(answer)

    def false_pressed(self):
       self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, answer):
        if answer:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)



