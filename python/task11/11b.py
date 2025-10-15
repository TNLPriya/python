import tkinter as tk

def add():
    try:
        result = float(num1_entry.get()) + float(num2_entry.get())
        result_label.config(text=f"Result: {result}")
    except ValueError:
        result_label.config(text="Please enter valid numbers!")

def subtract():
    try:
        result = float(num1_entry.get()) - float(num2_entry.get())
        result_label.config(text=f"Result: {result}")
    except ValueError:
        result_label.config(text="Please enter valid numbers!")

def multiply():
    try:
        result = float(num1_entry.get()) * float(num2_entry.get())
        result_label.config(text=f"Result: {result}")
    except ValueError:
        result_label.config(text="Please enter valid numbers!")

def divide():
    try:
        num1 = float(num1_entry.get())
        num2 = float(num2_entry.get())
        if num2 == 0:
            result_label.config(text="Cannot divide by zero!")
        else:
            result = num1 / num2
            result_label.config(text=f"Result: {result:.2f}")
    except ValueError:
        result_label.config(text="Please enter valid numbers!")

# Create main window
root = tk.Tk()
root.title("Basic Calculator")

# Input fields
tk.Label(root, text="Enter first number:").pack()
num1_entry = tk.Entry(root)
num1_entry.pack()

tk.Label(root, text="Enter second number:").pack()
num2_entry = tk.Entry(root)
num2_entry.pack()

# Operation buttons
tk.Button(root, text="Add (+)", bg="lightgreen", command=add).pack(pady=2)
tk.Button(root, text="Subtract (-)", bg="lightblue", command=subtract).pack(pady=2)
tk.Button(root, text="Multiply (×)", bg="orange", command=multiply).pack(pady=2)
tk.Button(root, text="Divide (÷)", bg="pink", command=divide).pack(pady=2)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
result_label.pack(pady=10)

root.mainloop()
