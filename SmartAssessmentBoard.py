import tkinter as tk
from tkinter import ttk

class StateCapital:
    def __init__(self, state, capital):
        self.state = state
        self.capital = capital

    def get_state(self):
        return self.state

    def get_capital(self):
        return self.capital

class QuizController:
    def __init__(self, questions):
        self.questions = questions
        self.current_question_index = 0
        self.score = 0

    def get_current_question(self):
        return self.questions[self.current_question_index]

    def check_answer(self, selected_answer):
        if selected_answer == self.get_current_question().get_capital():
            self.score += 1
        self.current_question_index += 1

    def get_score(self):
        return self.score

    def has_next_question(self):
        return self.current_question_index < len(self.questions)

class SmartAssessmentBoard:
    def __init__(self, controller):
        self.controller = controller

        self.root = tk.Tk()
        self.root.title("Smart Assessment Board")
        self.root.geometry("400x300")

        self.question_label = tk.Label(self.root, text="")
        self.question_label.pack(pady=20)

        self.answer_combo = ttk.Combobox(self.root)
        self.answer_combo.pack(pady=10)

        self.next_button = tk.Button(self.root, text="Next", command=self.next_question)
        self.next_button.pack(pady=20)

        self.score_label = tk.Label(self.root, text="Score: 0")
        self.score_label.pack(pady=10)

        self.load_question()

        self.root.mainloop()

    def load_question(self):
        question = self.controller.get_current_question()
        self.question_label.config(text=f"What is the capital of {question.get_state()}?")

        self.answer_combo['values'] = ["Select Capital", question.get_capital(), "Incorrect Capital 1", "Incorrect Capital 2"]
        self.answer_combo.current(0)  # Set default value

    def next_question(self):
        selected_answer = self.answer_combo.get()
        if selected_answer != "Select Capital":
            self.controller.check_answer(selected_answer)

            if self.controller.has_next_question():
                self.load_question()
            else:
                self.question_label.config(text="Quiz Complete!")
                self.answer_combo.config(state='disabled')
                self.next_button.config(state='disabled')

            self.score_label.config(text=f"Score: {self.controller.get_score()}")

if __name__ == "__main__":
    quiz_questions = [
        StateCapital("Andhra Pradesh", "Amaravati"),
        StateCapital("Bihar", "Patna"),
        StateCapital("Karnataka", "Bengaluru"),
        StateCapital("Maharashtra", "Mumbai"),
        StateCapital("Tamil Nadu", "Chennai")
        # Add more states and capitals here
    ]

    controller = QuizController(quiz_questions)
    SmartAssessmentBoard(controller)
