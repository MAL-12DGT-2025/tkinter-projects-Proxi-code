import tkinter as tk
from tkinter import ttk

def press(n):
    current = equation.get()

    symbols = ["+,""-","*","/"]

    
    if current [-1] in symbols:
        current.rstrip("+-*/")
        current= current + n
    equation.set(current)

def clear():
    equation.set("")

def calculate():
    try:
        result = eval(equation.get())
        equation.set(result)
    except:
        equation.set('ERROR')

root = tk.Tk()

root.title("Cookculator")

equation = tk.StringVar()

number = ttk.Entry(root, textvariable = equation)
number.grid(row=0, column=0, columnspan = 4)

Button_clr = ttk.Button(root, text = "CLR",  command = clear)
Button_clr.grid(row=4, column=0)

Button_0 = ttk.Button(root, text = "0",  command = lambda:press("0"))
Button_0.grid(row=4, column=1)   

Button_equal = ttk.Button(root, text = "=",  command = calculate)
Button_equal.grid(row=4, column=2) 

Button_plus = ttk.Button(root, text = "+",  command = lambda:press("+"))
Button_plus.grid(row=4, column=3) 

Button_1 = ttk.Button(root, text = "1",  command = lambda:press("1"))
Button_1.grid(row=3, column=0)       

Button_2 = ttk.Button(root, text = "2",  command = lambda:press("2"))
Button_2.grid(row=3, column=1) 

Button_3 = ttk.Button(root, text = "3",  command = lambda:press("3"))
Button_3.grid(row=3, column=2)
Button_neg = ttk.Button(root, text = "-",  command = lambda:press("-"))
Button_neg.grid(row=3, column=3)             

Button_4 = ttk.Button(root, text = "4",  command = lambda:press("4"))
Button_4.grid(row=2, column=0)   
                   
Button_5 = ttk.Button(root, text = "5",  command = lambda:press("5"))
Button_5.grid(row=2, column=1) 

Button_6 = ttk.Button(root, text = "6",  command = lambda:press("6"))
Button_6.grid(row=2, column=2) 

Button_time = ttk.Button(root, text = "*",  command = lambda:press("*"))
Button_time.grid(row=2, column=3)    

Button_7 = ttk.Button(root, text = "7",  command = lambda:press("7"))
Button_7.grid(row=1, column=0)   
                   
Button_8 = ttk.Button(root, text = "8",  command = lambda:press("8"))
Button_8.grid(row=1, column=1) 

Button_9 = ttk.Button(root, text = "9",  command = lambda:press("9"))
Button_9.grid(row=1, column=2) 

Button_divided = ttk.Button(root, text = "/",  command = lambda:press("/"))
Button_divided.grid(row=1, column=3)

root.mainloop()
