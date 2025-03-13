import tkinter as tk
from tkinter import ttk

def choice():
    player = con_var.get()

    if player == 0:
        print("Player chose Rock")
    elif player == 1:
        print("Player chose Paper")
    else:
        print("Player chose Scissor")

root = tk.Tk()

root.title("rock,paper scissor")

con_var = tk. IntVar(value = 1)

title =ttk.Label(root, text ="Rock paper scissor game")
title.grid(row=0, column=0, columnspan = 4)

rock = ttk.Button(root, text = "Rock", command = choice, value = 0, variable = con_var )
rock.grid(row=2, column=1)

paper = ttk.Button(root, text = "Paper", command = choice, value = 1, variable = con_var)
paper.grid(row=2, column=2)

scissor = ttk.Button(root, text = "Scissor", command = choice, value = 2, variable = con_var)
scissor.grid(row=2, column=3)

result_l = ttk.Label(root, text ="")
result_l.grid(row = 4, column = 0, columnspan = 2)

root.mainloop()
