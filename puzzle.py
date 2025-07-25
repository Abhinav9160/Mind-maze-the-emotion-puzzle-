import tkinter as tk
from tkinter import messagebox
import random

# Emotion scenarios
SCENARIOS = [
    {
        "question": "Your friend cancels plans last-minute. How do you respond?",
        "choices": [
            ("Get angry", 0),
            ("Understand they may have a reason", 1),
            ("Ignore them next time", 0)
        ]
    },
    {
        "question": "You made a mistake at work. What do you do?",
        "choices": [
            ("Blame someone else", 0),
            ("Admit it and fix it", 1),
            ("Ignore it", 0)
        ]
    },
    {
        "question": "You see someone being bullied. What do you do?",
        "choices": [
            ("Laugh", 0),
            ("Stand up for them", 1),
            ("Walk away quietly", 0)
        ]
    },
    {
        "question": "You get a bad grade. What’s your response?",
        "choices": [
            ("Give up", 0),
            ("Study harder next time", 1),
            ("Blame the teacher", 0)
        ]
    }
]

class MindMazeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("MindMaze: The Emotion Puzzle")
        self.root.geometry("600x400")
        self.score = 0
        self.current_room = 0
        self.total_rooms = len(SCENARIOS)

        self.create_widgets()

    def create_widgets(self):
        self.question_label = tk.Label(self.root, text="", wraplength=500, font=("Arial", 14))
        self.question_label.pack(pady=20)

        self.choice_var = tk.StringVar()
        self.choices_frame = tk.Frame(self.root)
        self.choices_frame.pack(pady=10)

        self.next_button = tk.Button(self.root, text="Next Room", command=self.next_room)
        self.next_button.pack(pady=20)

        self.load_room()

    def load_room(self):
        for widget in self.choices_frame.winfo_children():
            widget.destroy()

        if self.current_room < self.total_rooms:
            scenario = SCENARIOS[self.current_room]
            self.question_label.config(text=f"Room {self.current_room + 1}: {scenario['question']}")

            for text, value in scenario["choices"]:
                rb = tk.Radiobutton(
                    self.choices_frame,
                    text=text,
                    variable=self.choice_var,
                    value=f"{text}|{value}",
                    font=("Arial", 12),
                    anchor="w",
                    justify="left",
                    wraplength=500
                )
                rb.pack(anchor="w", pady=5)
            self.choice_var.set("")
        else:
            self.end_game()

    def next_room(self):
        selected = self.choice_var.get()
        if not selected:
            messagebox.showwarning("Choose an answer", "Please select an answer to proceed.")
            return

        choice_text, choice_value = selected.split("|")
        if int(choice_value) == 1:
            self.score += 1

        self.current_room += 1
        self.load_room()

    def end_game(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        result = f"Game Over!\nYou made {self.score} emotionally intelligent choices out of {self.total_rooms}."
        tk.Label(self.root, text=result, font=("Arial", 16), wraplength=500).pack(pady=50)

# Main
if __name__ == "__main__":
    root = tk.Tk()
    app = MindMazeGame(root)
    root.mainloop()
