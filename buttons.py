import tkinter as Tk
import sys
import os

# Add the directory containing the buttons module to the system path
sys.path.append(os.path.dirname("testing python.py"))

entry = Tk.Entry(root, width=50, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4)

button = Tk.Button(root, text="1", padx=40, pady=20)
button.grid(row=1, column=0)

button = Tk.Button(root, text="2", padx=40, pady=20)
button.grid(row=1, column=1)

button = Tk.Button(root, text="3", padx=40, pady=20)
button.grid(row=1, column=2)

button= Tk.Button(root, text="4", padx=40, pady=20)
button.grid(row=2, column=0)

button = Tk.Button(root, text="5", padx=40, pady=20)
button.grid(row=2, column=1)

button = Tk.Button(root, text="6", padx=40, pady=20)
button.grid(row=2, column=2)

button = Tk.Button(root, text="7", padx=40, pady=20)
button.grid(row=3, column=0)

button = Tk.Button(root, text="8", padx=40, pady=20)
button.grid(row=3, column=1)

button = Tk.Button(root, text="9", padx=40, pady=20)
button.grid(row=3, column=2)

button = Tk.Button(root, text="0", padx=40, pady=20)
button.grid(row=4, column=1)

button = Tk.Button(root, text="+/-", padx=35, pady=20)
button.grid(row=4, column=0)

button = Tk.Button(root, text=".", padx=40, pady=20)
button.grid(row=4, column=2)