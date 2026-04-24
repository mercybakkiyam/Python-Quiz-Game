from tkinter import *
from tkinter import messagebox
import turtle

questions = [
    "What is the correct syntax to output 'Hello World' in Python?",
    "Which data type is used to store a sequence of characters in Python?",
    "How do you start a comment in Python?",
    "What is the output of the expression 5 + 2 * 3?",
    "Which of the following is used to define a function in Python?"
]

options = [
    ["print('Hello World')", "echo 'Hello World'", "console.log('Hello World')", "write('Hello World')"],
    ["String", "Integer", "List", "Dictionary"],
    ["//", "#", "/*", "<!--"],
    ["11", "21", "17", "8"],
    ["function myFunction()", "define myFunction()", "def myFunction()", "func myFunction()"]
]

answers = [
    "print('Hello World')",
    "String",
    "#",
    "11",
    "def myFunction()"
]

window = Tk()
window.title("Quiz Game")
window.geometry("500x400")
window.configure(bg="#f0f8ff")

current_question = 0
score = 0
selected_option_var = IntVar()

def smile_face():
    turtle.clear()
    turtle.hideturtle()
    turtle.speed(0)
    turtle.setheading(0)  
    turtle.penup()
    turtle.goto(0, -100)  
    turtle.pendown()
    turtle.color("yellow")
    turtle.begin_fill()
    turtle.circle(100)
    turtle.end_fill()
   
    turtle.color("black")
    turtle.penup()
    turtle.goto(-35, 35)
    turtle.pendown()
    turtle.dot(10)

    turtle.penup()
    turtle.goto(35, 35)
    turtle.pendown()
    turtle.dot(10)
   
    turtle.penup()
    turtle.goto(-40, 0)
    turtle.pendown()
    turtle.setheading(270)  
    turtle.circle(40, 180)

def sad_face():
    turtle.clear()
    turtle.hideturtle()
    turtle.speed(0)
    turtle.setheading(0)
    turtle.penup()
    turtle.goto(0, -100)
    turtle.pendown()
    turtle.color("yellow")
    turtle.begin_fill()
    turtle.circle(100)
    turtle.end_fill()
   
    turtle.color("black")
    turtle.penup()
    turtle.goto(-35, 35)  
    turtle.pendown()
    turtle.dot(10)

    turtle.penup()
    turtle.goto(35, 35)
    turtle.pendown()
    turtle.dot(10)

    turtle.penup()
    turtle.goto(-38, -40)  
    turtle.pendown()
    turtle.setheading(270)  
    turtle.circle(40, -180)
   
title = Label(window, text="Quiz Game", font=("Arial", 20, "bold"), bg="#f0f8ff", fg="#333")
title.pack(pady=10)

question = Label(window, text="", wraplength=400, font=("Arial", 14), bg="#f0f8ff", fg="#333")
question.pack(pady=20)

options_frame = Frame(window, bg="#f0f8ff")
options_frame.pack(pady=10)

option_buttons = []
for i in range(4):
    button = Radiobutton(options_frame, text="", variable=selected_option_var, value=i, font=("Arial", 12), bg="#f0f8ff", fg="#000", anchor='w')
    button.pack(anchor='w', padx=10, pady=5) 
    option_buttons.append(button)
 
submit_button = Button(window, text="Submit", width=10, font=("Arial", 12), bg="#4169e1", fg="#fff")
submit_button.pack(pady=20)

def generate_question():
    global current_question
    question.config(text=questions[current_question])
   
    for i in range(4):
        option_buttons[i].config(text=options[current_question][i])
   
    selected_option_var.set(-1)

def submit():
    global current_question, score
    selected_option_index = selected_option_var.get()
    if selected_option_index == -1:
        messagebox.showwarning("Warning", "Please select an option!")
    else:
        selected_option = options[current_question][selected_option_index]    
        if selected_option == answers[current_question]:
            score += 1
            smile_face()
            messagebox.showinfo("Correct!", "That's the right answer!")
        else:
            sad_face()
            messagebox.showinfo("Wrong!", "Sorry, that's not correct.")
        current_question += 1

        if current_question < len(questions):
            generate_question()
        else:
            messagebox.showinfo("Quiz Completed", "Your score: " + str(score) + "/" + str(len(questions)))
            turtle.bye()
            window.destroy()  

submit_button.config(command=submit)
generate_question()
turtle.setup(width=400, height=400)
window.mainloop()
