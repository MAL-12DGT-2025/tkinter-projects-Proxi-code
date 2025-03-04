import tkinter as tk 
import tkinter as Tk

root = tk,Tk()

title = tk.Label(root, text ="Temperture\nConverter")
title.grid(row=0, column=0)
number = Tk.Entry(root)
number.grid(row = 1, column=0)

root.mainloop()