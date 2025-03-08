import math
import tkinter as Tk
from buttons import Calculator


root = Tk.Tk() 
root.title("Calculator")
root.geometry("420x600")


calc = Calculator(root)

root.mainloop()
    
