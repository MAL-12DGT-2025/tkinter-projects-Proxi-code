import tkinter as tk
from tkinter import ttk
import random

root = tk.Tk()

root.title("rock,paper scissor")

title =ttk.Label(root, text ="Rock paper scissor game")
title.grid(row=0, column=0, columnspan = 4)

rock = ttk.Button(root, text = "Rock")
rock.grid(row=2, column=1)

paper = ttk.Button(root, text = "Paper")
paper.grid(row=2, column=2)

scissor = ttk.Button(root, text = "Scissor")
scissor.grid(row=2, column=3)
root.mainloop()
