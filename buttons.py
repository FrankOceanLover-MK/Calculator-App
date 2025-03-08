import tkinter as Tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.calculated = False
        self.create_widgets()

    def create_widgets(self):
    # Entry field
        self.entry = Tk.Entry(self.root, font = ("Helvetica", 18), width=10, borderwidth=10, justify="right")
        self.entry.grid(row=0, column=0, columnspan=4, sticky="nsew")

    # Button layout (updated with correct `=` function)
        buttons = [
        ("1", 1, 0), ("2", 1, 1), ("3", 1, 2), ("+", 1, 3),
        ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("-", 2, 3),
        ("7", 3, 0), ("8", 3, 1), ("9", 3, 2), ("*", 3, 3),
        ("C", 4, 0), ("0", 4, 1), (".", 4, 2), ("/", 4, 3),
    ]

    # Create number and operation buttons
        for text, row, col in buttons:
            btn = Tk.Button(self.root, text=text, padx=20, pady=20,
                        command=lambda t=text: self.button_click(t))  # Correctly passes value
            btn.grid(row=row, column=col, sticky="nsew")

    # Clear button (C)
        clear_button = Tk.Button(self.root, text="C", padx=20, pady=20, command=self.clear_display)
        clear_button.grid(row=4, column=0, sticky="nsew")

    # Equals button (=) - Correctly calls `calculate_result()`
        equals_button = Tk.Button(self.root, text="=", padx=20, pady=20, command=self.calculate_result)
        equals_button.grid(row=5, column=0, columnspan=4, sticky="nsew")

    # Make grid rows and columns expandable
        for i in range(6):  # Number of rows
            self.root.grid_rowconfigure(i, weight=1)

        for j in range(4):  # Number of columns
            self.root.grid_columnconfigure(j, weight=1)


    def button_click(self, value):
    
        current = self.entry.get()

        if self.calculated:
            if value.isdigit() or value == ".":
                self.entry.delete(0, Tk.END)
                self.calculated = False

    # Check if an error message is displayed
        if current.startswith("Error"):
            self.entry.delete(0, Tk.END)  # Clear the error
            if value.isdigit() or value == ".":  # If the user presses a number, start fresh
                self.entry.insert(Tk.END, str(value))
                return  # Prevent appending extra characters after clearing
        
        

        self.entry.insert(Tk.END, str(value))  # Append new input normally

    def clear_display(self):
            self.entry.delete(0, Tk.END)

    def calculate_result(self):
        try:
            result = eval(self.entry.get())  # Evaluate the math expression
            self.entry.delete(0, Tk.END)  # Clear the entry field
            self.entry.insert(Tk.END, str(result))  # Display the result
            self.calculated = True  # Set the flag
        except ZeroDivisionError:
            self.entry.delete(0, Tk.END)
            self.entry.insert(Tk.END, "Error: Div by 0")  # Handle division by zero
            self.calculated = False
        except Exception:
            self.entry.delete(0, Tk.END)
            self.entry.insert(Tk.END, "Error")  # Handle other errors
            self.calculated = False
