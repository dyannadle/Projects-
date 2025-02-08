# Importing the library
import tkinter

# Window
root = tkinter.Tk()
root.title("QUIZ")
root.geometry('700x900')
c = 0
label_t = tkinter.Label(root, text="QUIZ", font=("arial", 50))
label_t.place(x=600, y=50)

# Label widget for user
label_u = tkinter.Label(root, text="Username", font=("arial", 30))
label_u.place(x=250, y=250)

# Entry widget
entry = tkinter.Entry(root, font=("arial", 30))
entry.place(x=500, y=250)


# Function to increase the point
def increase():
    global c
    c += 1


# Question 1
def info1():
    global c
    name = entry.get()
    label_q1 = tkinter.Label(root, text="Question 1", font=("Arial", 35))
    label_q1.place(x=550, y=50)
    label1 = tkinter.Label(root, text="Which of them is a Keyword in Python?", font=("Arial", 30))
    label1.place(x=300, y=100)

    # Button widget for options
    op1 = tkinter.Button(root, text="range", font=("Arial", 20), command=info2)
    op1.place(x=400, y=200)
    op2 = tkinter.Button(root, text="def", font=("Arial", 20), command=lambda: [info2(), increase()])
    op2.place(x=800, y=200)
    op3 = tkinter.Button(root, text="Val", font=("Arial", 20), command=info2)
    op3.place(x=400, y=300)
    op4 = tkinter.Button(root, text="to", font=("Arial", 20), command=info2)
    op4.place(x=800, y=300)

    label_t.destroy()
    label_u.destroy()
    entry.destroy()
    button.destroy()


# Question 2
def info2():
    global c, label_q1, label1, op1, op2, op3, op4
    c += 1
    label_q2 = tkinter.Label(root, text="Question 2", font=("Arial", 35))
    label_q2.place(x=550, y=50)
    label2 = tkinter.Label(root, text="Which of the following is built-in function in Python?", font=("Arial", 30))
    label2.place(x=300, y=100)

    # Button widget for options
    opp1 = tkinter.Button(root, text="factorial()", font=("Arial", 20), command=info3)
    opp1.place(x=400, y=200)
    opp2 = tkinter.Button(root, text="print()", font=("Arial", 20), command=lambda: [info3(), increase()])
    opp2.place(x=800, y=200)
    opp3 = tkinter.Button(root, text="seed()", font=("Arial", 20), command=info3)
    opp3.place(x=400, y=300)
    opp4 = tkinter.Button(root, text="sqrt()", font=("Arial", 20), command=info3)
    opp4.place(x=800, y=300)

    label_q1.destroy()
    label1.destroy()
    op1.destroy()
    op2.destroy()
    op3.destroy()
    op4.destroy()


# Question 3
def info3():
    global c, opp1, opp2, opp3, opp4, label_q2, label2
    c += 1
    label_q3 = tkinter.Label(root, text="Question 3", font=("Arial", 35))
    label_q3.place(x=550, y=50)
    label3 = tkinter.Label(root, text="Which of the following is not the core datatype in Python?",
                           font=("Arial", 30))
    label3.place(x=200, y=100)

    # Button widgets for options
    oppp1 = tkinter.Button(root, text="Tuple", font=("Arial", 20), width=8, command=info4)
    oppp1.place(x=400, y=200)
    oppp2 = tkinter.Button(root, text="Dictionary", font=("Arial", 20), width=7, command=info4)
    oppp2.place(x=800, y=200)
    oppp3 = tkinter.Button(root, text="Lists", font=("Arial", 20), width=7, command=info4)
    oppp3.place(x=400, y=300)
    oppp4 = tkinter.Button(root, text="Class", font=("Arial", 20), command=lambda: [info4(), increase()])
    oppp4.place(x=800, y=300)
    opp1.destroy()
    opp2.destroy()
    opp3.destroy()
    opp4.destroy()
    label_q2.destroy()
    label2.destroy()


# Question 4
def info4():
    global c, oppp1, oppp2, oppp3, oppp4, label_q3, label3
    c += 1
    label_q4 = tkinter.Label(root, text="Question 4", font=("Arial", 38))
    label_q4.place(x=550, y=50)
    label4 = tkinter.Label(root, text="Who developed python programming language?", font=("Arial", 35))
    label4.place(x=200, y=100)

    # Button widget for options
    opppp1 = tkinter.Button(root, text="Wick Van Rossum", font=("Arial", 20), command=info5)
    opppp1.place(x=400, y=200)
    opppp2 = tkinter.Button(root, text="Rasmus Lerdorf", font=("Arial", 20), command=info5)
    opppp2.place(x=800, y=200)
    opppp3 = tkinter.Button(root, text="Guido Van Rossum", font=("Arial", 20), command=lambda: [info5(), increase()])
    opppp3.place(x=400, y=300)
    opppp4 = tkinter.Button(root, text="Niene Stom", font=("Arial", 20), command=info5)
    opppp4.place(x=800, y=300)

    label_q3.destroy()
    label3.destroy()
    oppp1.destroy()
    oppp2.destroy()
    oppp3.destroy()
    oppp4.destroy()


# Question 5
def info5():
    global c, opppp1, opppp2, opppp3, opppp4, label_q4, label4
    c += 1
    label_q5 = tkinter.Label(root, text="Question 5", font=("Arial", 38))
    label_q5.place(x=550, y=50)
    label5 = tkinter.Label(root, text="Which of the following is the extension for Python File?",
                           font=("Arial", 35))
    label5.place(x=150, y=100)

    # Button widget for options
    oppppp1 = tkinter.Button(root, text=".python", font=("Arial", 20), width=15, command=info6)
    oppppp1.place(x=400, y=200)
    oppppp2 = tkinter.Button(root, text=".p", font=("Arial", 20), width=13, command=info6)
    oppppp2.place(x=800, y=200)
    oppppp3 = tkinter.Button(root, text=".pl", font=("Arial", 20), width=16, command=info6)
    oppppp3.place(x=400, y=300)
    oppppp4 = tkinter.Button(root, text=".py", font=("Arial", 20), width=10, command=lambda: [info6(), increase()])
    oppppp4.place(x=800, y=300)

    label_q4.destroy()
    label4.destroy()
    opppp1.destroy()
    opppp2.destroy()
    opppp3.destroy()
    opppp4.destroy()


# Displaying the score
def info6():
    global c, name, oppppp1, oppppp2, oppppp3, oppppp4, label_q5, label5
    label_q6 = tkinter.Label(root, text="SCORE", font=("Arial", 38), width=10)
    label_q6.place(x=550, y=50)
    label6 = tkinter.Label(root, text=name, font=("Arial", 35))
    label6.place(x=150, y=200)
    labell6 = tkinter.Label(root, text=c, font=("Arial", 30))
    labell6.place(x=400, y=200)

    label_q5.destroy()
    label5.destroy()
    oppppp1.destroy()
    oppppp2.destroy()
    oppppp3.destroy()
    oppppp4.destroy()


button = tkinter.Button(root, text="ENTER", font=("arial", 30), command=info1)
button.place(x=600, y=350)
root.mainloop()