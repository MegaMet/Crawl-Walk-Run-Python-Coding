THEME_COLOR = "#375362"
FONT = ("arial", 20, "italic")

from tkinter import *
from quiz_brain import QuizBrain

class QuizInterface():
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(pady= 20, padx= 20, bg= THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg= "white", bg= THEME_COLOR, font= FONT)
        self.score_label.grid(row= 0, column=1)

        self.canvas = Canvas(width= 300, height= 250, bg= "white")
        self.question_text = self.canvas.create_text(150, 125, text= "Some Question Text", width= 280, fill= THEME_COLOR, font= FONT)
        self.canvas.grid(row= 1, column= 0, columnspan= 2, pady= 50)

        true_image = PhotoImage(file= "images/true.png")
        self.button_true = Button(image= true_image, highlightthickness= 0, command= self.true_pressed)
        self.button_true.grid(row= 2, column= 0)
        false_image = PhotoImage(file= "images/false.png")
        self.button_false = Button(image= false_image, highlightthickness= 0, command= self.false_pressed)
        self.button_false.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text= q_text)
        else:
            self.canvas.itemconfig(self.question_text, text= "You've reached the end of the quiz!")
            self.button_true.config(state= "disabled")
            self.button_false.config(state= "disabled")

    def true_pressed(self):
        is_right = self.quiz.check_answer("true")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("false")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg= "green")
        else:
            self.canvas.config(bg= "red")
        self.window.after(2000, self.get_next_question)
