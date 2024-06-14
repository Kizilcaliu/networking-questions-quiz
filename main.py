import tkinter as tk
from tkinter import messagebox
from questions_data import questions
import random

# Shuffle the questions
random.shuffle(questions)

# Initialize variables
current_question = 0
score = 0

# Function to check answer and update score
def check_answer():
    global score, current_question
    
    selected_option = var.get()
    correct_answer = questions[current_question]["correct_answer"]
    
    if selected_option == correct_answer:
        score += 3
        feedback_label.config(text="Correct!", fg="green")
    else:
        score -= 1
        feedback_label.config(text=f"Wrong. Correct answer is: {correct_answer}", fg="red")
    
    # Disable radio buttons after answering
    for button in option_buttons:
        button.config(state=tk.DISABLED)
    
    # Proceed to next question after a delay for feedback
    root.after(1500, next_question)

# Function to proceed to the next question
def next_question():
    global current_question
    
    current_question += 1
    
    if current_question < len(questions):
        load_question()
    else:
        messagebox.showinfo("Quiz Completed", f"You have completed the quiz!\nYour score is: {score}")
        root.destroy()

# Function to load question and options
def load_question():
    question_label.config(text=questions[current_question]["question"])
    for i, option in enumerate(questions[current_question]["options"]):
        option_buttons[i].config(text=option, value=option, fg="black", state=tk.NORMAL)  # Set value to option string and reset color
    var.set(None)  # Clear selection
    feedback_label.config(text="")  # Clear previous feedback

# Create GUI
root = tk.Tk()
root.title("Networking and Security Quiz")

# Set fixed size for the GUI window
root.geometry("600x400")  # Width x Height

# Question label
question_label = tk.Label(root, text="", wraplength=580, justify="center", padx=10, pady=10)
question_label.pack()

# Radio buttons for options
var = tk.StringVar()
option_buttons = []
for i in range(4):
    option_button = tk.Radiobutton(root, text="", variable=var)
    option_button.pack(anchor=tk.W)
    option_buttons.append(option_button)

# Feedback label
feedback_label = tk.Label(root, text="", fg="black")
feedback_label.pack()

# Next button
next_button = tk.Button(root, text="Next", command=check_answer)
next_button.pack(pady=10)

# Load first question
load_question()

# Run the GUI
root.mainloop()
